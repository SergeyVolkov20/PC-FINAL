from django import forms
from .models import SimpleBooking
from django.utils import timezone

class BookingForm(forms.ModelForm):
    class Meta:
        model = SimpleBooking
        fields = ['full_name', 'phone', 'email', 'booking_date', 'booking_time', 'duration', 'guests', 'comments']
        widgets = {
            'booking_date': forms.DateInput(attrs={
                'type': 'date', 
                'min': timezone.now().date(),
                'class': 'form-control',
                'style': 'color: white !important;'
            }),
            'booking_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'style': 'color: white !important;'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше ФИО',
                'style': 'color: white !important;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (XXX) XXX-XX-XX',
                'style': 'color: white !important;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@mail.ru',
                'style': 'color: white !important;'
            }),
            'duration': forms.Select(attrs={
                'class': 'form-select',
                'style': 'color: white !important; background-color: #2d2d2d !important;'
            }),
            'guests': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 10,
                'style': 'color: white !important;'
            }),
            'comments': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Дополнительные пожелания...',
                'style': 'color: white !important;'
            }),
        }
        labels = {
            'full_name': 'ФИО',
            'phone': 'Телефон',
            'email': 'Email',
            'booking_date': 'Дата бронирования',
            'booking_time': 'Время бронирования', 
            'duration': 'Продолжительность (часы)',
            'guests': 'Количество гостей',
            'comments': 'Комментарии',
        }