# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404,render
from .models import Post, Category, Comment
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


class CategoryListView(ListView):
   template_name = 'blog_app/category_list.html'
   model = Category
   context_object_name = 'categories'


def post_list(request,pk):
    m_list = Post.objects.filter(category=pk)
    context = {'posts': m_list}
    return render(request, 'blog_app/post_list.html', context)


class NewPost(CreateView):
   template_name = 'blog_app/new_post.html'
   form_class = PostForm
   success_url = '/'

class EditPost(UpdateView):
   template_name = 'blog_app/edit_post.html'
   form_class = PostForm
   context_object_name = 'post'
   model = Post
   pk_field = 'pk'
   success_url = '/'


class PostDetails(DetailView):
   template_name = 'blog_app/details.html'
   model = Post
   context_object_name = 'post'
   pk_field = 'pk'

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('PostDetail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog_app/add_comment.html', {'form': form})

@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('PostDetail', pk=comment.post.pk)

@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('PostDetail', pk=comment.post.pk)