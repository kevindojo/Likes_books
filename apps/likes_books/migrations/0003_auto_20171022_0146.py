# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0002_auto_20171022_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='liked_users',
            field=models.ManyToManyField(null=True, related_name='liked_books', to='likes_books.User'),
        ),
        migrations.AlterField(
            model_name='book',
            name='uploaded_by_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_books_id', to='likes_books.User'),
        ),
    ]
