# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('look', '0003_auto_20170226_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookimage',
            name='order',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
