from django.core.cache import cache
from catalog.models import Products, Category
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Получаем список продуктов из кэша если он не пустой или из базы данных если пустой."""
    if not CACHE_ENABLED:
        return Products.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Products.objects.all()
    cache.set(key, products)
    return products


def get_categories_from_cache():
    """Получаем список категорий из кэша если он не пустой или из базы данных если пустой."""
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = "categories_list"
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories
