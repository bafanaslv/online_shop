from django.contrib import admin
from catalog.models import Category, Products, ProductVersion


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category",)
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(ProductVersion)
class ProductVersionAdmin(admin):
    list_display = ("id", "name", "version_number", "version_name", "current_version")
