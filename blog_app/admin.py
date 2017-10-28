# -*- coding: utf-8 -*-

# login - admin
# password - administrator

from __future__ import unicode_literals
from django.contrib import admin
from .models import Post, Comment, Category

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
