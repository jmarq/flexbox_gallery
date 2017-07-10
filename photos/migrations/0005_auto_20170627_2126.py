# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_photo_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='photo',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
