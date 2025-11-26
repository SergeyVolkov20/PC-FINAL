from django.contrib import admin
from .models import Price, ClubInfo, EquipmentCategory, Equipment, SimpleBooking  # ← ДОБАВИТЬ SimpleBooking

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('time_period', 'price', 'duration', 'is_dinner_price')
    list_filter = ('is_dinner_price',)

@admin.register(ClubInfo)
class ClubInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'equipment_type', 'specification', 'category', 'is_active')
    list_filter = ('equipment_type', 'category', 'is_active')

@admin.register(SimpleBooking)
class SimpleBookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'booking_date', 'booking_time', 'duration', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('full_name', 'phone', 'email')
    ordering = ('-created_at',)