# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-14 05:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hotline', '0005_auto_20181112_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='t_request',
            old_name='comment',
            new_name='comment1',
        ),
    ]
