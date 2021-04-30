from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView # Import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Invst, MF
from .forms import UserLoginForm, UserRegisterForm
from datetime import date


def loginView(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # if next:
            #     return redirect(next)
            # return HttpResponseRedirect(reverse('home'))
            return redirect('mf')
    context = {'form': form}
    return render(request, 'login.html', context)


def registerView(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')
            
    context = {'form': form}
    return render(request, 'login.html', context)

def logoutView(request):
    logout(request)
    return redirect('/')


def format_date(d):
    d = d.split('-')[::-1]
    d = [int(x) for x in d]
    return date(*d)

def format_num(num):
    return '{},{}'.format(str(num)[:-6], str(num)[-6:])

#@login_required
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
    # return render(request, 'testing.html')


#@login_required
def mfView(request):
    row = MF.objects.all()
    amount_total = 0
    for i in row:
        amount_total += i.amount
        i.amount = format_num(i.amount)
    context = {'row': row, 'amount_total':format_num(amount_total)}

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


def delInvestment(request, modelName, list_id):
    # // do nothing
    if request.method == 'GET':
        try:
            if(modelName == 'invst'): m = Invst
            elif (modelName == 'mf'): m = MF
            else: m = None
            m.objects.get(id=list_id).delete()
            return HttpResponseRedirect(reverse(modelName))
        except:
            return render(request, 'error.html')

        # if list_id in
    return HttpResponse('Hi')


def testing(request):
    invst = Invst.objects.all()
    mf = MF.objects.all()

    context = {'invst': invst, 'mf': mf} 
    return render(request, 'testing.html', context)
