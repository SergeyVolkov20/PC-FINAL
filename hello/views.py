from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ClubInfo, Equipment, SimpleBooking  
from .forms import BookingForm
from django.utils import timezone

def index(request):
    rooms = Equipment.objects.filter(equipment_type='room', is_active=True)
    hardware = Equipment.objects.filter(equipment_type='hardware', is_active=True)
    peripherals = Equipment.objects.filter(equipment_type='peripheral', is_active=True)
    
    context = {
        'club_name': 'COLIZEUM МИРА 55',
        'address': 'ПРОСПЕКТ МИРА 55, СУРГУТ',
        'description': 'COLIZEUM Сургут - это компьютерный клуб, оснащенный передовым оборудованием, которое соответствует всем требованиям современных игр.',
        'rooms': rooms,
        'hardware': hardware,
        'peripherals': peripherals,
    }
    return render(request, 'index.html', context)

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.status = 'pending'
            booking.save()
            messages.success(request, 'Бронирование успешно отправлено! Мы свяжемся с вами для подтверждения.')
            return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(request, 'booking.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')