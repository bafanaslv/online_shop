from django.shortcuts import render, get_object_or_404
from catalog.models import Products, Category
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Products
    template_name = 'products_list.html'

    @staticmethod
    def all_category():
        return Category.objects.all()


class CategoryProductListView(ListView):
    model = Products
    template_name = 'products_list.html'

    def get_queryset(self):
        cat = self.kwargs['category']
        queryset = Products.objects.filter(category=cat)
        return queryset

    @staticmethod
    def all_category():
        return Category.objects.all()


class ProductDetailView(DetailView):
    model = Products
    template_name = 'product_detail.html'

    @staticmethod
    def all_category():
        return Category.objects.all()


def product(request, pk):
    products = get_object_or_404(Products, pk=pk)
    context = {"product": products}
    return render(request, 'product_detail.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'contact.html')
