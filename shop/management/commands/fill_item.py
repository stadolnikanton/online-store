from django.core.management.base import BaseCommand
from shop.models import Product, ProductType

class Command(BaseCommand):
    help = 'Create 50 PC peripheral products'

    def handle(self, *args, **options):
        # Создаем или получаем тип товара
        product_type, created = ProductType.objects.get_or_create(
            title="Периферия для ПК"
        )
        
        if created:
            self.stdout.write('Created product type: Периферия для ПК')

        # Список тестовых товаров
        products_data = [
            # Мыши
            {'name': 'Мышь проводная Logitech M90', 'description': 'Надежная проводная мышь для офиса', 'price': 899.00, 'count': 30},
            {'name': 'Мышь беспроводная Razer DeathAdder', 'description': 'Игровая беспроводная мышь', 'price': 4599.00, 'count': 15},
            {'name': 'Мышь игровая SteelSeries Rival 3', 'description': 'Точная игровая мышь с RGB подсветкой', 'price': 3299.00, 'count': 20},
            {'name': 'Мышь офисная Defender WM-505', 'description': 'Эргономичная мышь для работы', 'price': 599.00, 'count': 45},
            {'name': 'Мышь беспроводная Microsoft Mobile Mouse', 'description': 'Компактная мышь для ноутбука', 'price': 2199.00, 'count': 25},
            
            # Клавиатуры
            {'name': 'Клавиатура проводная A4Tech KR-85', 'description': 'Надежная мембранная клавиатура', 'price': 1299.00, 'count': 40},
            {'name': 'Клавиатура механическая HyperX Alloy FPS', 'description': 'Механическая клавиатура для геймеров', 'price': 8999.00, 'count': 12},
            {'name': 'Клавиатура беспроводная Logitech K380', 'description': 'Универсальная Bluetooth клавиатура', 'price': 3499.00, 'count': 18},
            {'name': 'Клавиатура игровая Razer BlackWidow', 'description': 'Механика с переключателями Razer Green', 'price': 12999.00, 'count': 8},
            {'name': 'Клавиатура офисная Defender Oscar', 'description': 'Эргономичная клавиатура с подставкой', 'price': 1599.00, 'count': 35},
            
            # Наушники
            {'name': 'Наушники HyperX Cloud Stinger', 'description': 'Игровые наушники с микрофоном', 'price': 4299.00, 'count': 22},
            {'name': 'Наушники Sony WH-CH510', 'description': 'Беспроводные наушники с шумоподавлением', 'price': 5999.00, 'count': 16},
            {'name': 'Наушники JBL Tune 500BT', 'description': 'Стильные беспроводные наушники', 'price': 3499.00, 'count': 28},
            {'name': 'Наушники Razer Kraken X', 'description': 'Легкие игровые наушники 7.1', 'price': 5299.00, 'count': 14},
            {'name': 'Наушники Defender Warhead G-260', 'description': 'Бюджетные игровые наушники', 'price': 1599.00, 'count': 50},
            
            # Мониторы
            {'name': 'Монитор 24" Samsung LF24T350', 'description': 'IPS монитор с тонкими рамками', 'price': 15999.00, 'count': 10},
            {'name': 'Монитор 27" AOC 27B2H', 'description': 'Большой офисный монитор', 'price': 18999.00, 'count': 8},
            {'name': 'Монитор игровой 25" ASUS TUF Gaming', 'description': '144Hz для комфортной игры', 'price': 23999.00, 'count': 6},
            {'name': 'Монитор 21.5" HP 22MH', 'description': 'Компактный монитор для дома', 'price': 12999.00, 'count': 15},
            {'name': 'Монитор 32" LG UltraGear', 'description': '4K монитор для профессионалов', 'price': 45999.00, 'count': 4},
            
            # Колонки
            {'name': 'Колонки SVEN 312', 'description': 'Стерео колонки для ПК', 'price': 1299.00, 'count': 40},
            {'name': 'Колонки Defender Hurricane R35', 'description': 'Мощные колонки с сабвуфером', 'price': 3299.00, 'count': 25},
            {'name': 'Колонки Logitech Z213', 'description': '2.1 система с контролем низких частот', 'price': 4299.00, 'count': 18},
            {'name': 'Колонки Edifier R1280T', 'description': 'Студийные мониторы для меломанов', 'price': 12999.00, 'count': 12},
            {'name': 'Колонки Creative Pebble V3', 'description': 'Стильные USB-C колонки', 'price': 2999.00, 'count': 30},
            
            # Веб-камеры
            {'name': 'Веб-камера Logitech C270', 'description': 'HD камера для видео звонков', 'price': 3299.00, 'count': 35},
            {'name': 'Веб-камера A4Tech PK-333', 'description': 'Бюджетная веб-камера 720p', 'price': 1599.00, 'count': 50},
            {'name': 'Веб-камера Razer Kiyo', 'description': 'С кольцевой подсветкой для стримеров', 'price': 7999.00, 'count': 15},
            {'name': 'Веб-камера Microsoft LifeCam HD-3000', 'description': 'Надежная камера от Microsoft', 'price': 4299.00, 'count': 20},
            {'name': 'Веб-камера Trust GXT 1160 Thallo', 'description': '4K веб-камера с микрофоном', 'price': 11999.00, 'count': 8},
            
            # Коврики для мыши
            {'name': 'Коврик для мыши A4Tech X7-300', 'description': 'Большой игровой коврик', 'price': 899.00, 'count': 60},
            {'name': 'Коврик Razer Goliathus Extended', 'description': 'Протяженный коврик для клавиатуры и мыши', 'price': 3299.00, 'count': 25},
            {'name': 'Коврик SteelSeries QcK Heavy', 'description': 'Толстый коврик для точного контроля', 'price': 4299.00, 'count': 18},
            {'name': 'Коврик HyperX Fury S Pro', 'description': 'Гладкая поверхность для быстрых движений', 'price': 1999.00, 'count': 35},
            {'name': 'Коврик Defender Single', 'description': 'Стандартный коврик для офиса', 'price': 299.00, 'count': 100},
            
            # USB-хабы
            {'name': 'USB-хаб 4-port SVEN', 'description': 'Компактный USB концентратор', 'price': 799.00, 'count': 45},
            {'name': 'USB-хаб 7-port A4Tech', 'description': 'Хаб с индивидуальными выключателями', 'price': 1599.00, 'count': 30},
            {'name': 'USB-хаб Type-C Baseus', 'description': 'Современный хаб с разъемами USB-C', 'price': 2999.00, 'count': 22},
            {'name': 'USB-хаб Anker 10-port', 'description': 'Мощный хаб для всего оборудования', 'price': 5299.00, 'count': 15},
            {'name': 'USB-хаб Orico 4-port', 'description': 'Металлический хаб с защитой', 'price': 1299.00, 'count': 40},
            
            # Источники бесперебойного питания
            {'name': 'ИБП Powercom BNT-1000AP', 'description': 'Резервный ИБП для ПК', 'price': 8999.00, 'count': 12},
            {'name': 'ИБП Ippon Back Basic 650', 'description': 'Компактный ИБП для домашнего ПК', 'price': 5299.00, 'count': 18},
            {'name': 'ИБП APC Back-UPS 700', 'description': 'Надежный ИБП от американского бренда', 'price': 11999.00, 'count': 10},
            {'name': 'ИБП CyberPower UT650EI', 'description': 'Энергоэффективный ИБП', 'price': 7599.00, 'count': 14},
            {'name': 'ИБП Eaton 5S 700', 'description': 'Профессиональный ИБП для офиса', 'price': 13999.00, 'count': 8},
            
            # Внешние жесткие диски
            {'name': 'Внешний HDD Seagate 1TB', 'description': 'Портативный жесткий диск USB 3.0', 'price': 4299.00, 'count': 25},
            {'name': 'Внешний SSD Samsung T7 500GB', 'description': 'Скоростной SSD накопитель', 'price': 7999.00, 'count': 16},
            {'name': 'Внешний HDD WD Elements 2TB', 'description': 'Большой объем для архива', 'price': 6299.00, 'count': 20},
            {'name': 'Внешний SSD Kingston XS2000 1TB', 'description': 'Компактный SSD с высокой скоростью', 'price': 11999.00, 'count': 12},
            {'name': 'Внешний HDD Toshiba Canvio Basics 500GB', 'description': 'Надежный диск для повседневного использования', 'price': 3299.00, 'count': 30},
        ]

        # Создаем товары
        created_count = 0
        for product_info in products_data:
            product, created = Product.objects.get_or_create(
                name=product_info['name'],
                defaults={
                    'description': product_info['description'],
                    'price': product_info['price'],
                    'count': product_info['count'],
                    'product_types': product_type
                }
            )
            if created:
                created_count += 1
                self.stdout.write(f'Created: {product_info["name"]}')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} products')
        )
