from django.shortcuts import render
from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "body")
    success_url = reverse_lazy("catalog:products_list")


class BlogListView(ListView):
    model = Blog
