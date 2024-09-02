from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'Велосипеды', 'description': 'новые велосипеды'},
            {'category_name': 'Самокаты', 'description': 'новые самокаты'},
            {'category_name': 'Ролики', 'description': 'ролики, коньки'}
        ] 
        
        # Создаем категории
        categories = Category.objects.bulk_create([Category(**category) for category in category_list])

        products_list = [
            {'product_name': 'Веолосиед', 'product_description': 'новый', 'product_purchase_price': 5000.00, 'product_category_id': categories[1]},
            {'product_name': 'Самокат', 'product_description': 'б/у', 'product_purchase_price': 3000.00, 'product_category_id': categories[1]},
            {'product_name': 'Ролики', 'product_description': 'новые', 'product_purchase_price': 3500.00, 'product_category_id': categories[3]},
            {'product_name': 'Коньки', 'product_description': 'б/у, но как живые', 'product_purchase_price': 500.00, 'product_category_id': categories[3]},
            {'product_name': 'Велосипед', 'product_description': 'новый/детский', 'product_purchase_price': 5000.00, 'product_category_id': categories[1]},
        ]

        # Создаем продукты
        Product.objects.bulk_create([Product(**product) for product in products_list])
