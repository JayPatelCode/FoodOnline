from django import forms

from vendor.models import Vendor

class VendorForm(forms.ModelForm):
    class Meta:
        model=Vendor
        fields=['vendor_name', 'vendor_license']


# class OpeningHourForm(forms.ModelForm):
#     class Meta:
#         model = OpeningHour
#         fields = ['day', 'from_hour', 'to_hour', 'is_closed']