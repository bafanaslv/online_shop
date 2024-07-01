from django.shortcuts import render
from blog.models import Blog
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "body")
    success_url = reverse_lazy("catalog:products_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "body")
    success_url = reverse_lazy("catalog:products_list")


class BlogListView(ListView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
    # template_name = 'blog/confirm_delete.html'
    success_url = reverse_lazy("catalog:products_list")
