# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0006_auto_20170404_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchpost',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
