# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404,render
from .models import Post, Category, Comment
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView,UpdateView
from .forms import CategoryForm, PostForm, CommentForm


class CategoryListView(ListView):
   template_name = 'blog_app/category_list.html'
   model = Category
   context_object_name = 'categories'


# class PostListView(ListView):
#    template_name = 'blog_app/post_list.html'
#    model = Post
#    context_object_name = 'posts'
def post_list(request,pk):
    m_list = Post.objects.filter(category=pk)
    context = {'posts': m_list}
    return render(request, 'blog_app/post_list.html', context)

class NewPost(CreateView):
   template_name = 'blog_app/new_post.html'
   form_class = PostForm
   # change url
   success_url = '/'


class EditPost(UpdateView):
   template_name = 'blog_app/edit_post.html'
   form_class = PostForm
   context_object_name = 'post'
   # change url
   success_url = '/'
   model = Post
   pk_field = 'pk'


class PostDetails(DetailView):
   template_name = 'blog_app/details.html'
   model = Post
   context_object_name = 'post'
   pk_field = 'pk'
