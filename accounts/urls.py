########VENDOR#############
# testrest@email.com
# 123

########CUSTOMER#########
# jack@email.com       
# Jaypatel312003#

######logiN######
# http://localhost:8000/accounts/login/

######new email#######
# customer.foodcourt@gmail.com            12345
# OfflineFood@123
# agrb lewe xjne rahp
# jykv xjup xduo pgcc
# wnkq pevp dhuv wkcj

# django.foodcourt@gmail.com
# FoodOnline123@u8
# rtgw cnrx tzwy nuox

# vendor.foodcourt@gmail.com
# 123

# http://localhost:8000/accounts/registerUser/

from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.myAccount), 
    path("registerUser/", views.registerUser, name="registerUser"), 
    path("registerVendor/", views.registerVendor, name="registerVendor"),

    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("myAccount/", views.myAccount, name="myAccount"),
    path("custDashboard/", views.custDashboard, name="custDashboard"),
    path("vendorDashboard/", views.vendorDashboard, name="vendorDashboard"),
    path("activate/<uidb64>/<token>/",views.activate,name='activate'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('vendor/', include('vendor.urls')),
    # path('customer/', include('customers.urls')),
]
