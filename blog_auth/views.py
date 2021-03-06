# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404,render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .models import Post, Category, Comment, CustomUser
from .forms import PostForm, CommentForm, UserCreation

def add_like(request, pk):
    if request.user.is_authenticated():
        post = get_object_or_404(Post, pk=pk)
        if request.user not in post.user_likes.all():
            post.likes += 1
            post.user_likes.add(request.user)
            post.save()
        else:
            post.likes -= 1
            post.user_likes.remove(request.user)
            post.save()
    return redirect(request.GET.get('next', '/post/%s' %pk))


class SignUp(CreateView):
    template_name = "registration/register.html"
    model = CustomUser
    form_class = UserCreation
    success_url = "/"


class SignIn(LoginView):
    template_name = 'registration/login.html'


class CategoryListView(ListView):
   template_name = 'blog_auth/category_list.html'
   model = Category
   context_object_name = 'categories'


def post_list(request,pk):
    m_list = Post.objects.filter(category=pk)
    context = {'posts': m_list,
               'title': 'Our posts:',
               'category': m_list[0].category}
    return render(request, 'blog_auth/post_list.html', context)


class NewPost(CreateView):
   template_name = 'blog_auth/new_post.html'
   form_class = PostForm
   success_url = '/'


class EditPost(UpdateView):
   template_name = 'blog_auth/edit_post.html'
   form_class = PostForm
   context_object_name = 'post'
   model = Post
   pk_field = 'pk'
   success_url = '/'


class PostDetails(DetailView):
   template_name = 'blog_auth/details.html'
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
    return render(request, 'blog_auth/add_comment.html', {'form': form})

@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('PostDetail', pk=comment.post.pk)

def top(request):
    max_count = Post.objects.all().aggregate(max_likes=Max('likes'))
    top_posts = max_count.get('max_likes')
    result = Post.objects.filter(likes = top_posts).order_by('-published_date')[:3]
    context = {'posts': result,
               'title': 'Top 3 posts:',
               'category': 'all categories'}
    return render(request, 'blog_auth/post_list.html', context)
