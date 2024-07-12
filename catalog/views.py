from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.shortcuts import render
from catalog.forms import ProductsForm, ProductVersion
from catalog.models import Products, Category, ProductVersions
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse


class ProductListView(ListView):
    model = Products
    template_name = 'products_list.html'

    @staticmethod
    def all_category():
        return Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = object_list
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(self.kwargs)
    #     context['object_list'] = ProductVersions.objects.filter(name_id=self.kwargs['pk'])
    #     return context

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     versions = ProductVersions.objects.all()
    #     print(type(list(versions)[0]))
    #     # for prod in products:
    #     #     versions = ProductVersions.objects.filter(name_id=prod.id)
    #     #     if len(list(versions)) > 0:
    #     #         active_version = list(versions)[0]
    #     #     else:
    #     #         active_version = 'Нет активной версии'
    #     #
    #     # context_data['object_list'] = products
    #     return context_data


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
    form_class = ProductsForm
    template_name = 'product_create.html'
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductsForm
    template_name = 'product_create.html'
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        # return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])
        return reverse("catalog:products_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Products, ProductVersions, ProductVersion, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        # versions = ProductVersions.objects.filter(current_version=True, name=Products.objects.get(pk=self.object.pk))
        # print(len(versions))
        # if len(versions) > 2:
        #     raise ValidationError('У продукта не может быть более одной активной версии.')
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


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
