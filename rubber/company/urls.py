from django.urls import path
from . import views

urlpatterns = [
    path('company_login/', views.company_login, name='company_login'),
    path('company_register/', views.company_register, name='company_register'),
    path('company_home/', views.company_home, name='company_home'),
    path('natural_raw_materials/', views.natural_raw_materials, name='natural_raw_materials'),
    path('synthetic_raw_materials/', views.synthetic_raw_materials, name='synthetic_raw_materials'),
    path('natural_send_vendor/', views.natural_send_vendor, name='natural_send_vendor'),
    path('natural_company/<int:id>/', views.natural_company, name='natural_company'),
    path('synthetic_send_vendor/', views.synthetic_send_vendor, name='synthetic_send_vendor'),
    path('synthetic_company/<int:id>/', views.synthetic_company, name='synthetic_company'),
    path('company_logout/', views.company_logout, name='company_logout'),
    path('view_alternative_day_nal/', views.view_alternative_day_nal, name='view_alternative_day_nal'),
    path('send_mail_vendor_natural/<int:id>/', views.send_mail_vendor_natural,
         name='send_mail_vendor_natural'),
    path('view_alternative_day_syn/', views.view_alternative_day_syn, name='view_alternative_day_syn'),
    path('natural_send_process_unit/', views.natural_send_process_unit, name='natural_send_process_unit'),
    path('syn_send_process_unit/', views.syn_send_process_unit, name='syn_send_process_unit'),
    path('natural_company_process_unit/<int:id>/', views.natural_company_process_unit),
    path('syn_company_process_unit/<int:id>/', views.syn_company_process_unit)
]