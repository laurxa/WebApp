# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 02:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('citation', '0002_auto_20161102_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='slug',
            field=models.SlugField(editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='citation',
            unique_together=set([('user', 'slug')]),
        ),
    ]
