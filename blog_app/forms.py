from django import forms
from .models import Post, Category, Comment


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('title',)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post','author', 'text',)
