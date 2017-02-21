# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('poster_image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=500, null=True)),
                ('credits', models.CharField(blank=True, max_length=500, null=True)),
                ('detail', models.CharField(blank=True, max_length=500, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
    ]
