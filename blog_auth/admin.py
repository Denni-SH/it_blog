from django.contrib import admin
from .models import CustomUser, Category, Post, Comment

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
# Register your models here.
