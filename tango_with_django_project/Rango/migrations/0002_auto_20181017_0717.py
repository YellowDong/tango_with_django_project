# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='Rango.Category'),
        ),
    ]
