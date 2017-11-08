from django import forms
from .models import Post, Comment, CustomUser
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)


class UserCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')
