from django.shortcuts import render, reverse
from django.views.generic import TemplateView # Import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Invst, Dental, MF
from datetime import date


def format_date(d):
    d = d.split('-')[::-1]
    d = [int(x) for x in d]
    return date(*d)

def format_num(num):
    return '{},{}'.format(str(num)[:-6], str(num)[-6:])

def HomePageView(request):
    row = Invst.objects.all()
    amount_total = 0
    mat_total = 0
    for i in row:
        amount_total += i.amount
        mat_total += i.mat

        i.amount = format_num(i.amount)
        i.mat = format_num(i.mat)
    
    prof = round((mat_total - amount_total) / amount_total * 100, 2)
    context = {'row': row, 'amount_total':format_num(amount_total), 'mat_total':format_num(mat_total), 'prof':prof}

    return render(request, 'invst.html', context)

def dentalView(request):
    row = Dental.objects.all()
    for i in row:
        i.amount = format_num(i.amount)
    context = {'row': row}

    return render(request, 'dental.html', context)


def mfView(request):
    row = MF.objects.all()
    for i in row:
        i.amount = format_num(i.amount)
    context = {'row': row}

    return render(request, 'mf.html', context)


def addInvestment(request):
    if request.method == 'POST':
        row = Invst()
        row.date = format_date(request.POST['date'])
        row.rx = request.POST['rx']
        row.invst_type = request.POST['invst_type']
        row.amount = float(request.POST['amount'])
        row.mat = float(request.POST['maturity'])
        row.end_date = format_date(request.POST['end_date'])
        row.computeInvst()
        row.save()

        return HttpResponseRedirect(reverse('home'))

def addMF(request):
    if request.method == 'POST':
        row = MF()
        row.date = format_date(request.POST['date'])
        row.planName = request.POST['planName']
        row.amount = request.POST['amount']
        row.platform = request.POST['platform']
        if request.POST['lockin']: row.lockin = request.POST['lockin']
        row.save()

        return HttpResponseRedirect(reverse('mf'))

def addDental(request):
    if request.method == 'POST':
        row = Dental()
        row.date = format_date(request.POST['date'])
        row.rx = request.POST['rx']
        row.amount = request.POST['amount']
        row.save()

        return HttpResponseRedirect(reverse('dental'))


def delInvestment(request, modelName, list_id):
    # // do nothing
    if request.method == 'GET':
        try:
            if(modelName == 'invst'): m = Invst
            elif (modelName == 'mf'): m = MF
            elif (modelName == 'dental'): m = Dental
            else: m = None
            m.objects.get(id=list_id).delete()
            return HttpResponseRedirect(reverse(modelName))
        except:
            return render(request, 'error.html')


        # if list_id in
    return HttpResponse('Hi')