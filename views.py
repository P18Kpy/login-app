from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request,"base.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password']
        cpass = request.POST['cpassword']
        myuser = User.objects.create_user(username, email, pass1)
        myuser.firstname = fname
        myuser.lastname = lname
        myuser.save()
        
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect("login")
    return render(request,"signup.html")


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        
        user = authenticate(request,username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.firstname
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request,"login.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
