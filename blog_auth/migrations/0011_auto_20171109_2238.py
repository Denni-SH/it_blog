# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 22:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_auth', '0010_auto_20171109_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='I like '),
        ),
    ]
