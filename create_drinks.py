# create_drinks.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PC.settings')
django.setup()

from hello.models import Drink

drinks_data = [
    # Лимонады и безалкогольные коктейли
    {
        'name': 'Мохито классический',
        'description': 'Освежающий напиток с мятой, лаймом и содовой',
        'price': 280,
        'category': 'soda',
        'volume': '450 мл',
        'image_url': 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=400&h=300&fit=crop',
        'is_popular': True
    },
    {
        'name': 'Малиновый лимонад',
        'description': 'Домашний лимонад со свежей малиной',
        'price': 260,
        'category': 'soda',
        'volume': '500 мл',
        'image_url': 'https://images.unsplash.com/photo-1508254627334-1b5e508d3992?w-400&h=300&fit=crop',
        'is_popular': True
    },
    {
        'name': 'Пина Колада безалкогольная',
        'description': 'Тропический напиток с кокосом и ананасом',
        'price': 320,
        'category': 'soda',
        'volume': '450 мл',
        'image_url': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&h=300&fit=crop'
    },
    {
        'name': 'Имбирный лимонад',
        'description': 'Освежающий лимонад с имбирем и медом',
        'price': 240,
        'category': 'soda',
        'volume': '500 мл',
        'image_url': 'https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=400&h=300&fit=crop'
    },
    {
        'name': 'Дикая Вишня',
        'description': 'Лимонад с вишней и ванилью',
        'price': 290,
        'category': 'soda',
        'volume': '450 мл',
        'image_url': 'https://images.unsplash.com/photo-1514853035971-afb53a8d35e1?w=400&h=300&fit=crop',
        'is_popular': True
    },
    
    # Молочные коктейли
    {
        'name': 'Молочный коктейль Ванильный',
        'description': 'Нежный молочный коктейль с ванилью',
        'price': 320,
        'category': 'snack',
        'volume': '400 мл',
        'image_url': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&h=300&fit=crop',
        'is_popular': True
    },
    {
        'name': 'Молочный коктейль Шоколадный',
        'description': 'Шоколадный молочный коктейль с топпингом',
        'price': 340,
        'category': 'snack',
        'volume': '400 мл',
        'image_url': 'https://images.unsplash.com/photo-1592924357228-91a4daadcfea?w=400&h=300&fit=crop'
    },
    {
        'name': 'Молочный коктейль Клубничный',
        'description': 'Молочный коктейль со свежей клубникой',
        'price': 340,
        'category': 'snack',
        'volume': '400 мл',
        'image_url': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&h=300&fit=crop'
    },
    
    # Алкогольные коктейли
    {
        'name': 'Мохито алкогольный',
        'description': 'Классический мохито с ромом',
        'price': 420,
        'category': 'alcohol',
        'volume': '450 мл',
        'image_url': 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=400&h=300&fit=crop'
    },
    {
        'name': 'Пина Колада',
        'description': 'Тропический коктейль с ромом',
        'price': 450,
        'category': 'alcohol',
        'volume': '400 мл',
        'image_url': 'https://images.unsplash.com/photo-1470337458703-46ad1756a187?w=400&h=300&fit=crop'
    },
    
    # Кофе
    {
        'name': 'Эспрессо',
        'description': 'Крепкий черный кофе',
        'price': 180,
        'category': 'coffee',
        'volume': '50 мл',
        'image_url': 'https://images.unsplash.com/photo-1511537190424-bbbab87ac5eb?w=400&h=300&fit=crop'
    },
    {
        'name': 'Латте',
        'description': 'Кофе с молоком и пенкой',
        'price': 250,
        'category': 'coffee',
        'volume': '300 мл',
        'image_url': 'https://images.unsplash.com/photo-1568649929103-28ffbefaca1e?w=400&h=300&fit=crop',
        'is_popular': True
    },
    {
        'name': 'Капучино',
        'description': 'Кофе с молочной пенкой',
        'price': 230,
        'category': 'coffee',
        'volume': '250 мл',
        'image_url': 'https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=400&h=300&fit=crop'
    },
    
    # Чай
    {
        'name': 'Чай черный',
        'description': 'Чай черный с лимоном',
        'price': 120,
        'category': 'tea',
        'volume': '400 мл',
        'image_url': 'https://images.unsplash.com/photo-1597318181409-cf64d0b5d8a2?w=400&h=300&fit=crop'
    },
    {
        'name': 'Чай зеленый',
        'description': 'Зеленый чай с жасмином',
        'price': 120,
        'category': 'tea',
        'volume': '400 мл',
        'image_url': 'https://images.unsplash.com/photo-1597318181409-cf64d0b5d8a2?w=400&h=300&fit=crop'
    },
    
    # Энергетики
    {
        'name': 'Red Bull',
        'description': 'Энергетический напиток',
        'price': 200,
        'category': 'energy',
        'volume': '250 мл',
        'image_url': 'https://images.unsplash.com/photo-1622483767021-8b