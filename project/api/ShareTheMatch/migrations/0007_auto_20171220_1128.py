# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShareTheMatch', '0006_meetup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('supported_team', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='meetup',
            name='title',
            field=models.CharField(default='kek', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sport',
            name='meetup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sports', to='ShareTheMatch.Meetup'),
        ),
    ]