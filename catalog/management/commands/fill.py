from django.core.management import BaseCommand
from catalog.models import Category, Products
from django.db import connection
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open("catalog_category.json", 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open("catalog_products.json", 'r', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):

        product_for_create = []
        category_for_create = []
        cat_sequence = 1
        prod_sequence = 1
        self.clean_database()
        self.reset_sequences_cat(cat_sequence)
        self.reset_sequences_prod(prod_sequence)

        for category in Command.json_read_categories():
            category_for_create.append(Category(category["pk"],
                                                category["fields"]["name"],
                                                category["fields"]["description"]))
        Category.objects.bulk_create(category_for_create)
        self.reset_sequences_cat(len(category_for_create))

        for product in Command.json_read_products():
            product_for_create.append(Products(product["pk"],
                                               product["fields"]["name"],
                                               product["fields"]["description"],
                                               product["fields"]["category"],
                                               product["fields"]["image"],
                                               product["fields"]["price"],
                                               product["fields"]["owner"],
                                               product["fields"]["is_published"],
                                               product["fields"]["created_at"],
                                               product["fields"]["updated_at"]
                                               ))
        Products.objects.bulk_create(product_for_create)
        self.reset_sequences_prod(len(product_for_create))


    @staticmethod
    def reset_sequences_cat(cat_sequence):
        """Сихронизируем автоинкрементные значения таблицы категория"""
        with connection.cursor() as cursor:
            cursor.execute(f'ALTER SEQUENCE catalog_category_id_seq RESTART WITH {cat_sequence};')

    @staticmethod
    def reset_sequences_prod(prod_sequence):
        """Сихронизируем автоинкрементные значения таблицы продукты"""
        with connection.cursor() as cursor:
            cursor.execute(f'ALTER SEQUENCE catalog_products_id_seq RESTART WITH {prod_sequence};')

    @staticmethod
    def clean_database():
        """Очищаем базу данных"""
        Products.objects.all().delete()
        Category.objects.all().delete()
