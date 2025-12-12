from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking_view, name='booking'),  # Исправлено: booking_view
    path('booking/success/', views.booking_success, name='booking_success'),
    path('drinks/', views.drinks_menu, name='drinks_menu'),
    path('search/', views.search, name='search'),
    path('drinks/<int:drink_id>/', views.drink_detail, name='drink_detail')
]