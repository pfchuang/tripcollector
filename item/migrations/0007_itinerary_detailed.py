# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-10 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_auto_20180610_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='detailed',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
