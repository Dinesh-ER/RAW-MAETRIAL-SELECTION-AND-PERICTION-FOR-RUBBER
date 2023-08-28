from django.urls import path
from . import views

urlpatterns = [
    path('admin_home/', views.admin_home, name="admin_login"),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('approve_vendor/', views.approve_vendor, name='approve_vendor'),
    path('true_vendor/<int:id>/', views.true_vendor, name='true_vendor'),
    path('testing_table1_table2/', views.testing_table1_table2, name='testing_table1_table2'),
    path('matching/<int:id>/', views.matching ,name='matching'),
    path('matching_report/', views.matching_report),
    path('view_matching_report/<int:id>/', views.view_matching_report),
    path('matching_report_true/', views.matching_report_true),
    path('view_testing_matching_report_true/', views.view_testing_matching_report_true),
    path('admin_logout/', views.admin_logout, name='admin_logout')
    ]