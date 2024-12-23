from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from app_hotline.models import *

class RequestForm(ModelForm):
    class Meta:
        model = t_Request
        fields = '__all__'
        exclude = ('comment',)
        widgets = {
            'request_date': AdminDateWidget(),
            'patient_date': AdminDateWidget(),

        }
