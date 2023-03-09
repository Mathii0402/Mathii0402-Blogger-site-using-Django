import email
import re
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST['email']
        pass1=request.POST['pass']
        pass2=request.POST['pass-repeat']
        if pass1==pass2:
            if User.objects.filter(username=username):
                messages.warning(request,'username already exists!')
                return render(request,"register.html")
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.success(request,"user created successfully!!!")
                return render(request,"login.html")
        else:
            messages.error(request,"Password mismatched!")
            return render(request,"register.html") 
    else:
        return render(request,"register.html")

 
def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pass']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.error(request,'invalid credintials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')




def logout(request):
    auth.logout(request)
    return redirect('index.html')