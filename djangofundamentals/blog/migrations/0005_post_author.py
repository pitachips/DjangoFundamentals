# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-25 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='anonymous', max_length=20),
            preserve_default=False,
        ),
    ]