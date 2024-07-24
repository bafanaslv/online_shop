from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from catalog.forms import ProductsForm, ProductVersion, ProductModeratorForm
from catalog.models import Products, Category, ProductVersions
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse


class ProductListView(ListView):
    model = Products
    template_name = 'products_list.html'

    @staticmethod
    def all_category():
        return Category.objects.all()

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = self.get_queryset()
        for product in products:
            active_versions = ProductVersions.objects.filter(name_id=product.pk, current_version=True)
            if active_versions:
                product.active = active_versions.last().version_name
            else:
                product.active = 'Отсутствует'

        context_data['object_list'] = products
        return context_data


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


class ProductDetailView(DetailView, LoginRequiredMixin):
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

    def form_valid(self, form):
        product = form.save()
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'next'

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

    @transaction.atomic
    def form_valid(self, form, **kwargs):
        context_data = self.get_context_data(**kwargs)
        formset = context_data["formset"]
        product_versions = ProductVersions.objects.all()
        active_version_count = 0
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        for product in product_versions:
            if product.name_id == self.object.id and product.current_version:
                active_version_count += 1
        try:
            if active_version_count > 1:
                raise
        except active_version_count > 1:
            pass
        finally:
            if active_version_count < 2:
                return super().form_valid(form)
            else:
                transaction.set_rollback(True)
                form.add_error(None, 'У продукта не может быть более одной активной версии.')
                return self.form_invalid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductsForm
        if (user.has_perm("catalog.can_change_product_description")
                and user.has_perm("catalog.can_change_product_category")):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
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
