# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import post_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0002_auto_20180414_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=100, validators=[post_app.validators.validate_content]),
        ),
    ]
