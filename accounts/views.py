from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User


def registerUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # creating user using form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            #creating user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "You account has been successfully registered.")
            return redirect('registerUser') 

        else:
            messages.error(request, "There was an error during login.")
            print("Invalid form")
            print(form.errors)
    else:
        form = UserForm()
    context = {'form':form}
    return render(request,"accounts/registerUser.html",context)