
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("rubberapp.urls")),
    path("", include('vendor.urls')),
    path("", include('company.urls')),
    path("", include('process_unit.urls')),
    path("", include('admins.urls'))
]
