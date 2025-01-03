# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-08 03:53
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('request_date', models.DateField(default=datetime.date.today, verbose_name='Дата обращения')),
                ('number', models.PositiveIntegerField(verbose_name='Номер')),
                ('request_f', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('request_i', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('request_o', models.CharField(blank=True, max_length=50, verbose_name='Отчество')),
                ('request_s', models.BooleanField(verbose_name='Обращение по поводу себя')),
                ('patient_f', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('patient_i', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('patient_o', models.CharField(blank=True, max_length=50, verbose_name='Отчество')),
                ('patient_date', models.DateField(default=datetime.date.today, verbose_name='Дата обращения')),
                ('patient_work', models.CharField(blank=True, max_length=50, verbose_name='Место работы')),
                ('patient_position', models.CharField(blank=True, max_length=50, verbose_name='Должность')),
                ('patient_address', models.CharField(blank=True, max_length=50, verbose_name='Адрес')),
                ('patient_phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('question', models.TextField(blank=True, max_length=50, verbose_name='Вопрос')),
                ('result', models.CharField(blank=True, max_length=250, verbose_name='Результат')),
                ('age', models.CharField(choices=[('2', 'дети'), ('1', 'взрослые')], default='1', max_length=10, verbose_name='Вопрос по')),
                ('resolved', models.BooleanField(default=False, verbose_name='Решено положительно')),
                ('comment', models.BooleanField(default=False, verbose_name='Даны комментарии')),
                ('who_take', models.CharField(blank=True, max_length=50, verbose_name='Приём проводил(ФИО)')),
                ('Add', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
        migrations.CreateModel(
            name='s_clinic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('clinic', models.CharField(blank=True, max_length=50, verbose_name='Мед. учреждение')),
            ],
            options={
                'verbose_name': 'Мед. учреждение',
                'verbose_name_plural': 'Мед. учреждения',
            },
        ),
        migrations.CreateModel(
            name='s_Type_Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=50, verbose_name='Тип вопроса')),
            ],
            options={
                'verbose_name': 'Тип вопроса',
                'verbose_name_plural': 'Типы вопросов',
            },
        ),
        migrations.AddField(
            model_name='request',
            name='clinic',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_hotline.s_clinic', verbose_name='К какой медицинской организации жалоба'),
        ),
        migrations.AddField(
            model_name='request',
            name='type_request',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_hotline.s_Type_Request', verbose_name='Тип вопроса'),
        ),
    ]
