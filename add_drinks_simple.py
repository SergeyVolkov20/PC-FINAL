# add_drinks_simple.py
import os
import sys

# Добавляем путь к проекту
project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_path)

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first.settings')

try:
    import django
    django.setup()
    print("✓ Django настроен")
    
    from hello.models import Drink
    
    # Очищаем старые напитки (если есть)
    Drink.objects.all().delete()
    print("✓ Старые напитки удалены")
    
    # Создаем 8 популярных напитков
    drinks = [
        {
            'name': 'Мохито классический',
            'description': 'Освежающий напиток с мятой, лаймом и содовой. Идеально для жаркого дня.',
            'price': 280,
            'category': 'soda',
            'volume': '450 мл',
            'image_url': 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=400&h=400&fit=crop',
            'is_popular': True,
            'is_available': True
        },
        {
            'name': 'Малиновый лимонад',
            'description': 'Домашний лимонад с малиной и мятой. Свежий и вкусный напиток.',
            'price': 260,
            'category': 'soda',
            'volume': '500 мл',
            'image_url': 'https://images.unsplash.com/photo-1508254627334-1b5e508d3992?w=400&h=400&fit=crop',
            'is_popular': True,
            'is_available': True
        },
        {
            'name': 'Пина Колада безалкогольная',
            'description': 'Тропический напиток с кокосовым молоком и ананасом. Вкус лета!',
            'price': 320,
            'category': 'soda',
            'volume': '450 мл',
            'image_url': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&h=400&fit=crop',
            'is_popular': True,
            'is_available': True
        },
        {
            'name': 'Имбирный лимонад',
            'description': 'Освежающий лимонад с имбирем и медом. Тонизирует и бодрит.',
            'price': 240,
            'category': 'soda',
            'volume': '500 мл',
            'image_url': 'https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=400&h=400&fit=crop',
            'is_popular': False,
            'is_available': True
        },
        {
            'name': 'Дикая Вишня',
            'description': 'Лимонад с вишней и ванилью. Необычный вкус лесной ягоды.',
            'price': 290,
            'category': 'soda',
            'volume': '450 мл',
            'image_url': 'https://images.unsplash.com/photo-1514853035971-afb53a8d35e1?w=400&h=400&fit=crop',
            'is_popular': True,
            'is_available': True
        },
        {
            'name': 'Молочный коктейль Ванильный',
            'description': 'Нежный молочный коктейль с ванилью и мороженым.',
            'price': 320,
            'category': 'snack',
            'volume': '400 мл',
            'image_url': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&h=400&fit=crop',
            'is_popular': True,
            'is_available': True
        },
        {
            'name': 'Латте',
            'description': 'Кофе с молоком и нежной пенкой. Идеальный выбор для кофемана.',
            'price': 250,
            'category': 'coffee',
            'volume': '300 мл',
            'image_url': 'https://images.unsplash.com/photo-1568649929103-28ffbefaca1e?w=400&h=400&fit=crop',
            'is_popular': True,
            'is_available': True
        },
        {
            'name': 'Эспрессо',
            'description': 'Крепкий черный кофе. Для настоящих ценителей кофе.',
            'price': 180,
            'category': 'coffee',
            'volume': '50 мл',
            'image_url': 'https://images.unsplash.com/photo-1511537190424-bbbab87ac5eb?w=400&h=400&fit=crop',
            'is_popular': False,
            'is_available': True
        }
    ]
    
    # Создаем напитки
    for drink_data in drinks:
        Drink.objects.create(**drink_data)
        print(f"✓ Создан напиток: {drink_data['name']} - {drink_data['price']}₽")
    
    print(f"\n✅ Успешно создано {len(drinks)} напитков!")
    print("\nПопулярные напитки для главной страницы:")
    popular = Drink.objects.filter(is_popular=True)
    for drink in popular:
        print(f"  • {drink.name} - {drink.price}₽")
        
except Exception as e:
    print(f"✗ Ошибка: {e}")
    print("Возможные причины:")
    print("1. Убедитесь, что находитесь в папке проекта")
    print("2. Убедитесь, что имя проекта 'first'")
    print("3. Убедитесь, что есть файл settings.py в папке first")