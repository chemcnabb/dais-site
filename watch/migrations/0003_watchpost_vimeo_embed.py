# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_watchpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchpost',
            name='vimeo_embed',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
