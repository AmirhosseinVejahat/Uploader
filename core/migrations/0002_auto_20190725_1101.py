# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-25 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('author', models.CharField(default='', max_length=80)),
                ('topics', models.CharField(default='', max_length=50)),
                ('level', models.CharField(default='', max_length=50)),
                ('description', models.TextField()),
                ('duration', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
