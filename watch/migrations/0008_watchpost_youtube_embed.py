# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0007_watchpost_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchpost',
            name='youtube_embed',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
