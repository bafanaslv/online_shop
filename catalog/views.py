from django.shortcuts import render
from catalog.models import Products, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object
    #
    # def someview(request):
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ProductCreateView(CreateView):
    model = Products
    fields = ("category", "name",  "description", "image", "price")
    template_name = 'product_create.html'
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(UpdateView):
    model = Products
    fields = ("category", "name",  "description", "image", "price")
    template_name = 'product_create.html'
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy("catalog:products_list")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'contact.html')
