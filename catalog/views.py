from django.shortcuts import render
from catalog.models import Products, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse


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


class ContactViews(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
        return render(request, self.template_name)
