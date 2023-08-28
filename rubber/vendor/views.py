from django.shortcuts import render, redirect
from django.shortcuts import *
from . models import *
from django.db import IntegrityError
from django.contrib import messages
from company.models import *
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt, seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# Create your views here.


def vendor_home(request):
    return render(request,'vendor/vendor_home.html')


def vendor_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = register.objects.get(email=email, password=password)
            request.session['vendor'] = r.email
            if r is not None:
                messages.info(request, 'welcome')
                return redirect('/vendor_home/')
        except register.DoesNotExist as e:
            messages.info(request, 'Email does not exists')
            return redirect('/vendor_login/')
        else:
            messages.info(request, 'waiting for admin approve')
            return redirect('/vendor_login/')
    else:
        return render(request, 'vendor/login.html')


def vendor_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        age = request.POST['age']
        address = request.POST['address']
        password = request.POST['password']
        try:
            register(username=username, email=email, contact_no=contact_no, age=age, address=address,
                   password=password).save()
            messages.info(request, "successfully created")
            return redirect('/vendor_login/')
        except IntegrityError as e:
            messages.info(request, "Email already exists")
            return redirect('/vendor_register/')
    return render(request, 'vendor/login.html')


def vendor_logout(request):
    if 'vendor' in request.session:
        request.session.pop('vendor',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/vendor_logout/')


def view_natural(request):
    natural = natural_rubber.objects.all()
    if 'vendor' in request.session:
        natural = natural_rubber.objects.all()
    return render(request, 'vendor/view_generator.html', {'natural': natural})


def generate_natural_id(request,id):
    st = natural_rubber.objects.get(id=id)
    r = random.randint(1000,2000)
    st.natural_id = r
    st.save()
    return redirect('/vendor_home/')


def view_synthetic(request):
    synthetic = synthetic_rubber.objects.all()
    if 'vendor' in request.session:
        synthetic = synthetic_rubber.objects.all()
    return render(request, 'vendor/view_syn_supplyid.html', {'synthetic': synthetic})


def generate_synthetic_id(request,id):
    st = synthetic_rubber.objects.get(id=id)
    r = random.randint(1000,2000)
    st.syn_id = r
    st.save()
    return redirect('/vendor_home/')


def give_email(request, id):
    sd = natural_rubber.objects.get(id=id)
    reg = register.objects.get(id=id)
    # print(reg.email)
    a = reg.email
    print(a)
    natural_rubber(give_vendor=a).save()
    return redirect('/vendor_home/')


def give_email_syn(request, id):
    sd = natural_rubber.objects.get(id=id)
    reg = register.objects.get(id=id)
    # print(reg.email)
    a = reg.email
    print(a)
    natural_rubber(give_vendor_email=a).save()
    return redirect('/vendor_home/')


def view_natural_rubber(request):
    natural = natural_rubber.objects.all()
    if 'vendor' in request.session:
        natural = natural_rubber.objects.all()
    return render(request, 'vendor/view_natural_materials.html', {'natural': natural})


def view_synthetic_rubber(request):
    synthetic = synthetic_rubber.objects.filter(send_synthetic=True)
    if 'vendor' in request.session:
        synthetic = synthetic_rubber.objects.filter(send_synthetic=True)
    return render(request, 'vendor/view_synthetic_materials.html', {'synthetic': synthetic})


def check_availability(request, id):
    if request.method == "POST":
        availability = request.POST['availability']
        print(availability, "1")
        print(id)
        data1 = natural_rubber.objects.get(id=id)
        data1.availability = availability
        data1.save()
        a = data1.need_latex
        b = data1.availability
        print(a)
        print(b)
        remaining = int(a) - int(b)
        data1.remaining = remaining
        print(remaining)
        data1.check_remaining = True
        data1.save()
    return render(request, 'vendor/view_natural_materials.html')


def check_availability_syn(request, id):
    if request.method == "POST":
        availability = request.POST['availability']
        print(availability, "1")
        print(id)
        data1 = synthetic_rubber.objects.get(id=id)
        data1.availability = availability
        data1.save()
        a = data1.need_chemical
        b = data1.availability
        print(a)
        print(b)
        remaining = int(a) - int(b)
        data1.remaining = remaining
        data1.check_remaining = True
        data1.save()
    return render(request, 'vendor/view_synthetic_materials.html')


def view(request):
    natural = natural_rubber.objects.all()
    return render(request, 'vendor/alternative_day.html', {'natural': natural})


def view1(request):
    synthetic = synthetic_rubber.objects.all()
    return render(request, 'vendor/set_syn_alterday.html', {'synthetic': synthetic})


def fixing_date_natural(request,id):
    if request.method == "POST":
        fixing_date = request.POST['fixing_date']
        print(fixing_date, "1")
        data = natural_rubber.objects.get(id=id)
        data.fixing_date = fixing_date
        data.save()
    return render(request,'vendor/alternative_day.html')


def fixing_date_synthetic(request,id):
    if request.method == "POST":
        fixing_date1 = request.POST['fixing_date1']
        print(fixing_date1, "1")
        data = synthetic_rubber.objects.get(id=id)
        data.fixing_date1 = fixing_date1
        data.save()
    return render(request,'vendor/set_syn_alterday.html')


def send_fixing_date_natural(request):
    values = natural_rubber.objects.filter(send_fixing_date=False)
    if 'vendor' in request.session:
        values = natural_rubber.objects.filter(send_fixing_date=False)
        return render(request,'vendor/send_alternative_day.html',{'values': values})
    return render(request, 'vendor/send_alternative_day.html', {'values': values})


def disappear_fixing_date_natural(request, id):
    if "vendor" in request.session:
        values = natural_rubber.objects.get(id=id)
        values.send_fixing_date = True
        values.save()
        messages.info(request, "sent to alternative day for raw materials")
        return redirect('/send_fixing_date_natural/')


def send_fixing_date_synthetic(request):
    values = synthetic_rubber.objects.filter(send_fixing_date1=False)
    if 'vendor' in request.session:
        values = synthetic_rubber.objects.filter(send_fixing_date1=False)
        return render(request,'vendor/send_alter_syn.html',{'values': values})
    return render(request, 'vendor/send_alter_syn.html', {'values': values})


def disappear_fixing_date_syn(request, id):
    if "vendor" in request.session:
        values = synthetic_rubber.objects.get(id=id)
        values.send_fixing_date1 = True
        values.save()
        messages.info(request, "sent to alternative day for raw materials")
        return redirect('/send_fixing_date_synthetic/')


def graph_view(request):
    return render(request, 'vendor/graph.html')


def view_graph(request):
    
    df1 = pd.read_csv("Month Natural Rubber.csv")
    sns.scatterplot(x='year', y='total', data=df1)
    plt.show()
  
    return redirect('/graph_view/')


def vendor_natural_graph(request):
    # if 'vendor' in request.session:
    values = register.objects.filter(graph1=False)
    return render(request,'vendor/graph.html',{'values': values})


def send_natural_graph(request,id):
    # if "vendor" in request.session:
    values = register.objects.get(id=id)
    values.graph1 = True
    values.save()
    messages.info(request, "successfully sent to admin")
    return redirect('/vendor_home/')


def view_graph1(request):
    # df2 = pd.DataFrame(pd.read_excel("Natural Rubber Production.xlsx"))
    # read_file = pd.read_excel("Natural Rubber Production.xlsx")
    # read_file.to_csv("Natural Rubber Production.csv", header=True, index=False)
    # df3 = pd.DataFrame(pd.read_csv("Natural Rubber Production.csv"))
    df3 = pd.read_csv("Natural Rubber Production.csv")
    sns.scatterplot(x='Date', y='Metric Tons', data=df3)
    plt.show()
    return redirect('/graph_view/')


def vendor_syn_graph(request):
    if 'vendor' in request.session:
        values = register.objects.filter(graph2=False)
        return render(request,'vendor/graph.html',{'values': values})


def send_syn_graph(request,id):
    if "vendor" in request.session:
        values = register.objects.get(id=id)
        values.graph2 = True
        values.save()
        messages.info(request, "successfully sent to admin")
        return redirect('/vendor_syn_graph/')


def view_graph2(request):
    # df4 = pd.DataFrame(pd.read_excel("Synthetic Rubber.xlsx"))
    # read_file = pd.read_excel("Synthetic Rubber.xlsx")
    # read_file.to_csv("Synthetic Rubber.csv", header=True, index=False)
    # df5 = pd.DataFrame(pd.read_csv("Synthetic Rubber.csv"))
    df5 = pd.read_csv("Synthetic Rubber.csv")
    sns.scatterplot(x='year', y='Total', data=df5)
    plt.show()
    return redirect('/graph_view/')


def vendor_syn_nan_graph(request):
    if 'vendor' in request.session:
        values = register.objects.filter(graph3=False)
        return render(request,'vendor/graph.html',{'values': values})


def send_syn_nan_graph(request,id):
    if "vendor" in request.session:
        values = register.objects.get(id=id)
        values.graph3 = True
        values.save()
        messages.info(request, "successfully sent to admin")
        return redirect('/vendor_syn_nan_graph/')









