# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_auth', '0005_auto_20171109_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=0, verbose_name='I dislike'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='I like '),
        ),
    ]