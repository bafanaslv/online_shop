from django.shortcuts import render
from blog.models import Blog
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "body", "image")
    success_url = reverse_lazy("blog:list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "body", "image")
    success_url = reverse_lazy("blog:list")


class BlogListView(ListView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/confirm_delete.html'
    success_url = reverse_lazy("blog:list")


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object

