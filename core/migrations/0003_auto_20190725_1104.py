# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-25 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190725_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='duration',
            field=models.DurationField(),
        ),
    ]
