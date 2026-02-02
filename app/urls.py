
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('frontpage/', include('app.frontpage.urls')),
    path('staff/', include('app.staff.urls')),


]
