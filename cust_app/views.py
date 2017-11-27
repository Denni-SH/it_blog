from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import CustomUser

class SignForm(CreateView):
    template_name = 'blog_app/new_post.html'
    model = CustomUser
    context_object_name = 'categories'