from django.http import HttpResponse
from django.shortcuts import render

from vendor.models import Vendor
def home(request):
    vendor = Vendor.objects.filter(is_approved=True,user__is_active=True)
    print(vendor)
    context = {
        'vendors':vendor
    }
    return render(request,"home.html",context=context)