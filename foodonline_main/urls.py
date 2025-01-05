"""
password:12345
Username: admin
Email address: jay.patel@email.com
"""
from django.contrib import admin
from django.urls import path
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home')
]
