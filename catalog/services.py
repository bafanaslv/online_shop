from django.core.cache import cache
from catalog.models import Products
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Получаем данные из кэша если он не пустой и из базы данных если пустой."""
    if not CACHE_ENABLED:
        return Products.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Products.objects.all()
    cache.set(key, products)
    return products
