# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-22 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_booksorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksorder',
            name='isbn',
            field=models.CharField(max_length=50),
        ),
    ]
