from django.shortcuts import render, redirect
from django.shortcuts import *
from .models import *
from django.db import IntegrityError
from django.contrib import messages
from company.models import *
# Create your views here.
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')
from sklearn.neural_network import MLPClassifier


def process_home(request):
    return render(request,'process/process_home.html')


def process_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = unit_register.objects.get(email=email, password=password)
            request.session['process'] = r.email
            print(request.session['process'])
            if r is not None:
                messages.info(request, 'welcome')
                return redirect('/process_home/')
        except unit_register.DoesNotExist as e:
            messages.info(request, 'Email does not exists')
            return redirect('/process_login/')

    else:
        return render(request, 'process/login.html')


def process_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        age = request.POST['age']
        address = request.POST['address']
        password = request.POST['password']
        try:
            unit_register(username=username, email=email, contact_no=contact_no, age=age, address=address,
                   password=password).save()
            messages.info(request, "successfully created")
            return redirect('/process_login/')
        except IntegrityError as e:
            messages.info(request, "Email already exists")
            return redirect('/process_register/')
    return render(request, 'process/login.html')


def syn_view_process_unit(request):
    if 'process' in request.session:
        synthetic = synthetic_rubber.objects.filter(send_process_syn=True)
        return render(request,'process/view_synthetic.html', {"synthetic":synthetic})


def natural_view_process_unit(request):
    if 'process' in request.session:
        natural = natural_rubber.objects.filter(send_process_nal=True)
        return render(request,'process/view_natural.html', {"natural":natural})


def process_logout(request):
    if 'process' in request.session:
        request.session.pop('process',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/process_logout/')


def analyse_form(request):
    if request.method == "POST":
        property = request.POST['property']
        recycle = request.POST['recycle']
        compound = request.POST['compound']
        chemical_formula = request.POST['chemical_formula']
        polymer = request.POST['polymer']
        mixing = request.POST['mixing']
        made_from_type = request.POST['made_from_type']
        type=request.POST['type']
        analyse_rubber(property=property,recycle=recycle, compound=compound,chemical_formula=chemical_formula,
        polymer=polymer,mixing=mixing, made_from_type=made_from_type,type=type).save()
    return render(request, 'process/analyse_form.html')


def view_analyse_form(request):
    if 'process' in request.session:
        natural = analyse_rubber.objects.all()
        return render(request,'process/view_analyse_form.html', {"natural":natural})


def algo(datas,r):
    data = pd.read_csv('final.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = MLPClassifier()
    model.fit(data_x, data_y)

    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    print(12334455)
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]


df = pd.DataFrame(pd.read_excel("final.xlsx"))
read_file = pd.read_excel("final.xlsx")
read_file.to_csv("final.csv", header=True, index=False)


def disapper_analyse_form(request, id):
    natural = analyse_rubber.objects.get(id=id)
    natural.send_analyse = True
    natural.save()
    r=natural.id
    inputvar = []
    property = natural.property
    recycle = natural.recycle
    compound = natural.compound
    chemical_formula = natural.chemical_formula
    polymer = natural.polymer
    mixing = natural.mixing
    made_from_type = natural.made_from_type
    type = natural.type
    inputvar.append(property)
    inputvar.append(recycle)
    inputvar.append(compound)
    inputvar.append(chemical_formula)
    inputvar.append(polymer)
    inputvar.append(mixing)
    inputvar.append(made_from_type)
    inputvar.append(type)
    print('input:', inputvar)
    f=algo(inputvar,r)
    print('OUTPUT:',f)
    st = analyse_rubber.objects.filter(id=r).update(rubber_type=f)
    # return render(request,'process/view_analyse_form.html', {'natural': natural})
    return redirect('/view_analyse_form/')


def testing_analyse_form(request):
    if request.method == "POST":
        property = request.POST['property']
        recycle = request.POST['recycle']
        compound = request.POST['compound']
        chemical_formula = request.POST['chemical_formula']
        polymer = request.POST['polymer']
        mixing = request.POST['mixing']
        made_from_type = request.POST['made_from_type']
        type=request.POST['type']
        testing_rubber(property=property,recycle=recycle, compound=compound,chemical_formula=chemical_formula,
        polymer=polymer,mixing=mixing, made_from_type=made_from_type,type=type).save()
    return render(request, 'process/testing_analyse_form.html')


def send_to_admin_testing(request):
    if 'process' in request.session:
        synthetic = testing_rubber.objects.filter(send_testing=False)
        return render(request,'process/send_to_matching.html', {"synthetic":synthetic})


def true_admin_testing(request,id):
    if "process" in request.session:
        synthetic = testing_rubber.objects.get(id=id)
        synthetic.send_testing = True
        synthetic.save()
        messages.info(request, "successfully sent to admin")
        return redirect('/send_to_admin_testing/')