from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import ClubInfo, Equipment, Bookings, User, GamingStation 
from .forms import WebsiteBookingForm 

def index(request):
    """Главная страница"""
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
    
    rooms = Equipment.objects.filter(equipment_type='room', is_active=True)
    hardware = Equipment.objects.filter(equipment_type='hardware', is_active=True)
    peripherals = Equipment.objects.filter(equipment_type='peripheral', is_active=True)
    
    try:
        total_stations = GamingStation.objects.count()
        total_users = User.objects.count()
        total_bookings = Bookings.objects.count()
    except Exception as e:
        total_stations = rooms.count()
        total_users = 0  
        total_bookings = 0 
        print(f"Ошибка загрузки PC.db данных: {e}")
    
    context = {
        'club_info': club_info,
        'rooms': rooms,
        'hardware': hardware,
        'peripherals': peripherals,
        'total_stations': total_stations,
        'total_users': total_users,
        'total_bookings': total_bookings,
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