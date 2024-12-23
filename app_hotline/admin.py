from django.contrib import admin
from .models import  *

class Request_Admin(admin.ModelAdmin):


    # все видят все обращения
    """
    def get_queryset(self, request):
        if request.user.is_superuser:
            return Request.objects.all()
        else:
            return Request.objects.filter(Add=request.user)
    """

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'Add', None) is None:
            obj.Add = request.user
        obj.save()

    fieldsets = [
        ('', {'fields': [('request_date', 'number'),
                         ]}),

        ('Обратившийся',
         {'fields': ['request_f', 'request_i', 'request_o', 'request_s']}),

        ('Пациент',
         {'fields': ['patient_f', 'patient_i', 'patient_o', 'patient_date', ('patient_work', 'patient_position'),
                     ('patient_address', 'patient_phone'),
                      ('age', 'type_request')
                     ]}),

        ('', {'fields': ['clinic', 'question', 'result', 'who_take', ('resolved', 'comment1'),
                         ]}),

    ]

    list_display = ('number', 'request_date', 'request_f', 'patient_f', 'resolved', 'comment1')
    search_fields = ['request_date', 'patient_f', 'request_f']

    list_per_page = 20
    view_on_site = True
    date_hierarchy = 'request_date'
    list_display_links = ('number', 'request_date', 'patient_f', 'request_f')


admin.site.register(t_Request, Request_Admin)
admin.site.register(s_clinic)
admin.site.register(s_Type_Request)



# Register your models here.
