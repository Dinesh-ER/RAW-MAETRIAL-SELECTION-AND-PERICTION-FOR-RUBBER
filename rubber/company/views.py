from django.shortcuts import render, redirect
from django.shortcuts import *
from . models import *
from django.db import IntegrityError
from django.contrib import messages
from django.core.mail import send_mail
from vendor.models import *


def company_home(request):
    return render(request,'company/company_home.html')

def company_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = co_register.objects.get(email=email, password=password)
            request.session['company'] = r.email
            if r is not None:
                messages.info(request, 'welcome')
                return redirect('/company_home/')
        except co_register.DoesNotExist as e:
            messages.info(request, 'Email does not exists')
            return redirect('/company_login/')

    else:
        return render(request, 'company/login.html')


def company_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        age = request.POST['age']
        address = request.POST['address']
        password = request.POST['password']
        try:
            co_register(username=username, email=email, contact_no=contact_no, age=age, address=address,
                   password=password).save()
            messages.info(request, "successfully created")
            return redirect('/company_login/')
        except IntegrityError as e:
            messages.info(request, "Email already exists")
            return redirect('/company_register/')
    return render(request, 'company/login.html')


def natural_raw_materials(request):

    regi = co_register.objects.all()
    if request.method == "POST":
        latex_method = request.POST['latex_method']
        email = request.POST['email']
        latex_char = request.POST['latex_char']
        acid = request.POST['acid']
        Time_taken = request.POST['Time_taken']
        polymer = request.POST['polymer']
        industry = request.POST['industry']
        product = request.POST['product']
        type_of_trees = request.POST['type_of_trees']
        type_of_plants = request.POST['type_of_plants']
        property = request.POST['property']
        need_latex = request.POST['need_latex']
        natural_rubber(latex_method=latex_method, email= email,latex_char=latex_char, acid=acid, Time_taken=Time_taken, polymer=polymer,
        industry=industry,product=product, type_of_trees=type_of_trees, type_of_plants=type_of_plants, property=property, need_latex=need_latex).save()
    return render(request, 'company/raw_material.html', {"regi":regi})


def synthetic_raw_materials(request):
    regi = co_register.objects.all()
    if request.method == "POST":
        mineral_type = request.POST['mineral_type']
        email = request.POST['email']
        polymer_type = request.POST['polymer_type']
        gases = request.POST['gases']
        industry = request.POST['industry']
        product = request.POST['product']
        storage_type = request.POST['storage_type']
        chemical_type = request.POST['chemical_type']
        property = request.POST['property']
        rubber_type = request.POST['rubber_type']
        duration = request.POST['duration']
        need_chemical = request.POST['need_chemical']
        synthetic_rubber(mineral_type=mineral_type,polymer_type=polymer_type,
                        gases=gases,rubber_type=rubber_type,duration=duration,
                        industry=industry,product=product, storage_type=storage_type,
                        chemical_type=chemical_type, property=property, email=email, 
                        need_chemical=need_chemical).save()
    return render(request, 'company/synthetic_raw_material.html',{"regi":regi})


def company_logout(request):
    if 'company' in request.session:
        request.session.pop('company',None)
        messages.success(request, 'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/company_logout/')

def natural_send_vendor(request):
    if 'company' in request.session:
        natural = natural_rubber.objects.filter(send_natural=False)
        return render(request,'company/send_to_vendor_natural.html', {"natural":natural})

def natural_company(request,id):
    if 'company' in request.session:
        natural = natural_rubber.objects.get(id=id)
        natural.send_natural = True
        natural.save()
        messages.info(request, "send to vendor in natural_rubber raw materials details")
        return redirect('/natural_send_vendor/')

def synthetic_send_vendor(request):
    if "company" in request.session:
        synthetic = synthetic_rubber.objects.filter(send_synthetic=False)
        return render(request, 'company/send_to_vendor_syn.html', {"synthetic":synthetic})

def synthetic_company(request,id):
    if 'company' in request.session:
        synthetic = synthetic_rubber.objects.get(id=id)
        synthetic.send_synthetic = True
        synthetic.save()
        messages.info(request, "send to vendor in synthetic rubber raw material details")
        return redirect("/synthetic_send_vendor/")


def view_alternative_day_nal(request):
    if "company" in request.session:
        natural = natural_rubber.objects.filter(send_fixing_date=True)
        return render(request, 'company/view_natural_alternativeday.html', {"natural":natural})


def view_alternative_day_syn(request):
    if "company" in request.session:
        synthetic = synthetic_rubber.objects.filter(send_fixing_date1=True)
        return render(request, 'company/view_synthetic_alternative_day.html', {"synthetic":synthetic})


def natural_send_process_unit(request):
    if 'company' in request.session:
        natural = natural_rubber.objects.filter(send_process_nal=False)
        return render(request,'company/nat_send_to_process_unit.html', {"natural":natural})


def natural_company_process_unit(request,id):
    if 'company' in request.session:
        natural = natural_rubber.objects.get(id=id)
        natural.send_process_nal = True
        natural.save()
        messages.info(request, "send to process unit in natural rubber raw materials details")
        return redirect('/natural_send_process_unit/')


def syn_send_process_unit(request):
    if 'company' in request.session:
        synthetic = synthetic_rubber.objects.filter(send_process_syn=False)
        return render(request,'company/syn_send_to_process_unit.html', {"synthetic":synthetic})


def syn_company_process_unit(request,id):
    if 'company' in request.session:
        synthetic = synthetic_rubber.objects.get(id=id)
        synthetic.send_process_syn = True
        synthetic.save()
        messages.info(request, "send to process unit in synthetic rubber raw materials details")
        return redirect('/syn_send_process_unit/')


def send_mail_vendor_natural(request, id):
    if "company" in request.session:
        natural = register.objects.get(id=id)
        msg1 = '''You have allocated alternate day  for remaining raw materials,
                    make sure to confirm the order on the particular day'''

        send_mail(
            'Subject here',
            msg1,
            "authentication4email@gmail.com",
            [natural.email],
            fail_silently=False,
        )
        natural.mail_vanish = True
        natural.save()
        messages.info(request, "Sucessfully Sent To Vendor")

        return redirect("/view_alternative_day_nal/")


def send_mail_synthetic(request, id):
    if "company" in request.session:
        natural = register.objects.get(id=id)

        msg1 = '''You have allocated alternate day  for remaining raw materials,
                    make sure to confirm the order on the particular day'''
        
        send_mail('Subject here',msg1,"authentication4email@gmail.com",[natural.email],fail_silently=False,)
        natural.mail_vanish = True
        natural.save()
        messages.info(request, "Sucessfully Sent To Vendor")
        return redirect("/view_alternative_day_syn/")




