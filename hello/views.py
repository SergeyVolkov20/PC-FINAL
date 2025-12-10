from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from .models import ClubInfo, Equipment, Bookings, User, GamingStation, Drink
from .forms import WebsiteBookingForm, DrinkSearchForm

def index(request):
    """Главная страница"""
    # Получаем информацию о клубе
    club_info, created = ClubInfo.objects.get_or_create(
        name='COLIZEUM МИРА 55',
        defaults={
            'address': 'ПРОСПЕКТ МИРА 55, СУРГУТ',
            'description': 'COLIZEUM Сургут - это компьютерный клуб, оснащенный передовым оборудованием',
            'phone': '+7 (999) 123-45-67',
            'email': 'info@colizeum.ru',
            'working_hours': '24/7'
        }
    )
    
    # Получаем оборудование
    rooms = Equipment.objects.filter(equipment_type='room', is_active=True)
    hardware = Equipment.objects.filter(equipment_type='hardware', is_active=True)
    peripherals = Equipment.objects.filter(equipment_type='peripheral', is_active=True)
    
    # Статистика
    try:
        total_stations = GamingStation.objects.count()
        total_users = User.objects.count()
        total_bookings = Bookings.objects.count()
    except Exception as e:
        total_stations = rooms.count()
        total_users = 0  
        total_bookings = 0 
        print(f"Ошибка загрузки PC.db данных: {e}")
    
    # Получаем популярные напитки для главной страницы
    popular_drinks = Drink.objects.filter(is_available=True, is_popular=True)[:6]
    
    context = {
        'club_info': club_info,
        'rooms': rooms,
        'hardware': hardware,
        'peripherals': peripherals,
        'total_stations': total_stations,
        'total_users': total_users,
        'total_bookings': total_bookings,
        'popular_drinks': popular_drinks,
        'description': 'COLIZEUM Сургут - это компьютерный клуб, оснащенный передовым оборудованием',
        'address': 'Проспект Мира 55, Сургут',
    }
    return render(request, 'hello/index.html', context)

def booking_view(request):
    """Страница бронирования"""
    if request.method == 'POST':
        form = WebsiteBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False) 
            booking.status = 'pending'
            booking.save() 
            
            messages.success(request, 'Бронирование успешно отправлено! Мы свяжемся с вами для подтверждения.')
            return redirect('booking_success')
    else:
        form = WebsiteBookingForm()
    
    return render(request, 'hello/booking.html', {'form': form})

def booking_success(request):
    """Страница успешного бронирования"""
    return render(request, 'hello/booking_success.html')

def drinks_menu(request):
    """Страница с меню напитков"""
    form = DrinkSearchForm(request.GET or None)
    drinks = Drink.objects.filter(is_available=True)
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        category = form.cleaned_data.get('category')
        
        if query:
            drinks = drinks.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if category:
            drinks = drinks.filter(category=category)
    
    # Группируем по категориям для отображения
    categories = {}
    for drink in drinks:
        category_display = drink.get_category_display()
        if category_display not in categories:
            categories[category_display] = []
        categories[category_display].append(drink)
    
    context = {
        'drinks': drinks,
        'categories': categories,
        'form': form,
    }
    return render(request, 'hello/drinks_menu.html', context)

def search(request):
    """Поиск по сайту"""
    query = request.GET.get('q', '')
    
    # Здесь можно добавить логику поиска по разным моделям
    if query:
        # Пример поиска напитков
        drinks_results = Drink.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query),
            is_available=True
        )[:10]
        
        context = {
            'query': query,
            'drinks_results': drinks_results,
            'has_results': drinks_results.exists(),
        }
    else:
        context = {
            'query': '',
            'has_results': False,
        }
    
    return render(request, 'hello/search_results.html', context)