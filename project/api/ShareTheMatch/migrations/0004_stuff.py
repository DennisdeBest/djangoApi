# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShareTheMatch', '0003_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tv', models.CharField(max_length=100)),
                ('sits', models.CharField(max_length=500)),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stuffs', to='ShareTheMatch.Adress')),
            ],
        ),
    ]