from django.shortcuts import render, get_object_or_404
from catalog.models import Products


def products_list(request):
    context = {"products": Products.objects.all()}
    return render(request, 'products_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'contact.html')
