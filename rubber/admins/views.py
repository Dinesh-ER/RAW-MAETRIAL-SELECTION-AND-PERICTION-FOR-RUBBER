from django.shortcuts import render,redirect
from django.contrib import messages
from vendor. models import *
from process_unit. models import *
# Create your views here.


def admin_home(request):
    return render(request, 'admin/admin_home.html')


def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        if email == "admin@gmail.com" and password == "admin":
            print(email)
            request.session['admin'] = "admin@gmail.com"
            messages.info(request, "Successfully Registered ")
            return render(request,'admin/admin_home.html')
        elif email != "admin@gmail.com":
            messages.error(request, "Wrong Mail id")
            return render (request,'admin/login.html')
        elif password != "admin":
            messages.error(request,"wrong password")
            return render (request, 'admin/login.html')
        else:
            return render(request,'admin/login.html')
    return render(request,'admin/login.html')


def approve_vendor(request):
    if 'admin' in request.session:
        values = register.objects.filter(vendor_approve=False)
        return render(request,'admin/approve_vendor.html',{'values': values})


def true_vendor(request,id):
    if "admin" in request.session:
        values = register.objects.get(id=id)
        values.vendor_approve = True
        values.save()
        messages.info(request, "successfully approved for vendor")
        return redirect('/approve_vendor/')


def admin_logout(request):
    if 'admin' in request.session:
        request.session.pop('admin',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/admin_logout/')


def testing_table1_table2(request):
    if 'admin' in request.session:
        value = analyse_rubber.objects.all()
        values = testing_rubber.objects.all()
        return render(request, 'admin/testing.html', {'value':value,'values': values})


def matching(request, id):
    if 'admin' in request.session:
        value = analyse_rubber.objects.filter(send_report=False)
        values = testing_rubber.objects.get(id=id)
        r = values.id
        print(values.property)
        for i in value:
            i.send_report=True
            i.save()
            print(i.property, 1)
            if i.property == values.property and i.recycle == values.recycle and\
                    i.compound == values.compound and i.polymer== values.polymer:
                f = i.rubber_type
                print(f)
                st = testing_rubber.objects.filter(id=r).update(output=f)
                messages.info(request, 'successfully added your recommend')
                print(st)
            else:
                messages.info(request, 'No Matching for our materials')

        return redirect('/testing_table1_table2/')


def matching_report (request):
    if 'admin' in request.session:
        values = testing_rubber.objects.filter(matching=False)
        return render(request,'admin/testing.html',{'values': values})


def view_matching_report (request,id):
    if "admin" in request.session:
        values = testing_rubber.objects.get(id=id)
        values.matching = True
        values.save()
        messages.info(request, "successfully sent")
        return redirect('/matching_report/')


def matching_report_true (request):
    if 'admin' in request.session:
        values = testing_rubber.objects.filter(matching=True)
        return render(request,'admin/matching_report.html',{'values': values})


def view_testing_matching_report_true(request):
    if 'admin' in request.session:
        values = testing_rubber.objects.filter(send_testing=True)
        return render(request,'admin/view_testing_report.html',{'values': values})
