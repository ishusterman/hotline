from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .form import *
import datetime
from django.db.models import Max
from django.contrib.auth import logout
from django.shortcuts import redirect

def date_convert_to_usa(date):
    date = date.split(".")
    res=date[2]+"-"+date[1]+"-"+date[0]
    return res


def logoff(request):
    logout(request)
    return redirect('/index/')

@login_required(login_url='/login/')
def index(request):

    now = datetime.datetime.now()
    date1= "01.01." +str(now.year)
    date2 = str(now.day)+ "." +str(now.month)+ "."+str(now.year)
    count_rec_all = t_Request.objects.all().count()

    if 'filter' in request.POST:
        start_date = date_convert_to_usa(request.POST['start_date'])
        end_date = date_convert_to_usa(request.POST['end_date'])
        date1 = request.POST['start_date']
        date2 = request.POST['end_date']
        hotline = t_Request.objects.filter(request_date__gte=start_date).filter(request_date__lte=end_date)
        count_rec_cur = hotline.count()

    else:
        hotline=t_Request.objects.all()
        count_rec_cur = count_rec_all

    context = {'hotline': hotline, 'User': request.user, 'date1': date1, 'date2': date2, 'count_rec_cur': count_rec_cur, 'count_rec_all': count_rec_all}
    return render(request, 'index.html', context)

def edit(request, id):

    if id != "0":
        inst = t_Request.objects.get(id=id)
        form = RequestForm(instance=inst)

        # берем номер для формы редактирования
        if inst is not None:
            max = inst.number

    else:
        # новое обращение
        form = RequestForm()
        # находим мах +1 значение номера обращения для подстановки в поле
        # по умолчанию - 0
        max = t_Request.objects.all().aggregate(Max('number'))
        max = max.get('number__max', 0) + 1





    return render(request, 'edit.html',
                  {'item': form, 'id': id, 'number': max})


def save(request):

    id = request.POST['id']
    if id != "0":
        a = t_Request.objects.get(id=id)
    else:
        a = t_Request()

    action = request.POST['action']

    if action == "К списку":
        return redirect('/index/')
    if action == "Сохранить":

        f = RequestForm(request.POST, instance=a)
        if f.is_valid() :
            res = f.save()
            id = str(res.id)
        else:
            print (f.errors)

    return redirect('/request/edit/' + id)