# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='name',
            field=models.CharField(blank=True, default='Home', max_length=500, null=True),
        ),
    ]
