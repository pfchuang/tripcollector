# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-22 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_itinerary_detailed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateField()),
                ('status', models.CharField(max_length=10)),
                ('link', models.URLField()),
                ('price', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='day',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='departure_date',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='link',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='month',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='status',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='year',
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='travel_date',
            name='itinerary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Itinerary'),
        ),
    ]
