from django.core.management import BaseCommand
from catalog.models import Category, Products
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

        for category in Command.json_read_categories():
            category_for_create.append(Category(category["pk"],
                                                category["fields"]["name"],
                                                category["fields"]["description"]))
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(Products(product["pk"],
                                               product["fields"]["name"],
                                               product["fields"]["description"],
                                               product["fields"]["category"],
                                               product["fields"]["image"],
                                               product["fields"]["price"],
                                               product["fields"]["owner"],
                                               product["fields"]["created_at"],
                                               product["fields"]["updated_at"]
                                               ))
        Products.objects.bulk_create(product_for_create)
