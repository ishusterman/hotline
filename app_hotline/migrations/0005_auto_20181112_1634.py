# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-12 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hotline', '0004_auto_20181112_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_request',
            name='age',
            field=models.CharField(choices=[('дети', 'дети'), ('взрослые', 'взрослые')], default='взрослые', max_length=10, verbose_name='Вопрос по'),
        ),
    ]
