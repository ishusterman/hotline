from django.db import models
from datetime import date
from django.contrib.auth.models import User
import select2.fields
import select2.models

# Create your models here.


class s_clinic(models.Model):
    id = models.AutoField(primary_key=True)
    clinic = models.CharField(verbose_name="Мед. учреждение", max_length=50, blank=True)

    def __str__(self):
        return self.clinic

    class Meta:
        verbose_name = 'Мед. учреждение'
        verbose_name_plural = 'Мед. учреждения'

class s_Type_Request(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(verbose_name="Тип вопроса", max_length=50, blank=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип вопроса'
        verbose_name_plural = 'Типы вопросов'


class t_Request(models.Model):

    id = models.AutoField(primary_key=True)
    request_date = models.DateField(verbose_name="Дата обращения", default=date.today)
    number = models.PositiveIntegerField(verbose_name="Номер", blank=False)

    request_f = models.CharField(verbose_name="Фамилия", max_length=50, blank=True,)
    request_i = models.CharField(verbose_name="Имя", max_length=50, blank=True,)
    request_o = models.CharField(verbose_name="Отчество", max_length=50, blank=True,)
    request_s = models.BooleanField(verbose_name="Обращение по поводу себя", blank=True,)

    patient_f = models.CharField(verbose_name="Фамилия", max_length=50, blank=True,)
    patient_i = models.CharField(verbose_name="Имя", max_length=50, blank=True,)
    patient_o = models.CharField(verbose_name="Отчество", max_length=50, blank=True,)

    patient_date = models.DateField(verbose_name="Дата обращения", default=date.today)


    patient_work = models.CharField(verbose_name="Место работы", max_length=50, blank=True,)
    patient_position = models.CharField(verbose_name="Должность", max_length=50, blank=True,)
    patient_address = models.CharField(verbose_name="Адрес", max_length=50, blank=True,)
    patient_phone = models.CharField(verbose_name="Телефон", max_length=50, blank=True,)

    clinic = models.ForeignKey(s_clinic, verbose_name="К какой медицинской организации жалоба", default=None, blank=True, null=True)

    question = models.TextField(verbose_name="Вопрос", max_length=550, blank=True,)
    result = models.CharField(verbose_name="Результат", max_length=250, blank=True,)

    adult = 'взрослые'
    kids = 'дети'
    AGE_CHOICES = (
            (kids, 'дети'),
            (adult, 'взрослые'),
        )
    age = models.CharField(verbose_name="Вопрос по", max_length=10, choices=AGE_CHOICES, default=adult, blank=False)

    type_request = models.ForeignKey(s_Type_Request, verbose_name="Тип вопроса", default=None,
                               blank=True, null=True)



    resolved = models.BooleanField(verbose_name="Решено положительно", default=False)
    comment1 = models.BooleanField(verbose_name="Даны комментарии", default=False)

    who_take = models.CharField(verbose_name="Приём проводил(ФИО)", max_length=50, blank=True)

    Add = models.ForeignKey(User, null=True, blank=True, default=None)

    def __str__(self):
        return str(self.number) + " " +str(self.request_date)+ " " + str(self.request_f)+ " " +str(self.patient_f)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __unicode__(self):
        return self.id