from django.urls import path
from . import views

urlpatterns = [
    path('process_login/', views.process_login, name='process_login'),
    path('process_register/', views.process_register, name='process_register'),
    path('process_home/', views.process_home, name='process_home'),
    path('syn_view_process_unit/', views.syn_view_process_unit),
    path('natural_view_process_unit/', views.natural_view_process_unit),
    path('process_logout/', views.process_logout),
    path('analyse_form/', views.analyse_form),
    path('view_analyse_form/', views.view_analyse_form),
    path('disapper_analyse_form/<int:id>/', views.disapper_analyse_form),
    path('testing_analyse_form/', views.testing_analyse_form),
    path('send_to_admin_testing/', views.send_to_admin_testing),
    path('true_admin_testing/<int:id>/', views.true_admin_testing)
    ]