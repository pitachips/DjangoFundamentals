# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-26 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0004_post_user_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_agent',
            field=models.CharField(max_length=200),
        ),
    ]
