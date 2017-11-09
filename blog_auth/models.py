# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from  django.contrib.auth.models import *
from django.contrib.contenttypes.models import ContentType


class CustomUser(AbstractUser):
    objects = UserManager()


class Category(models.Model):
    title = models.CharField(max_length=20, default='Indefined')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    likes = models.IntegerField(verbose_name='I like ', default=0)
    user_likes = models.ManyToManyField(CustomUser, blank=True, related_name='post_likes')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.text)

