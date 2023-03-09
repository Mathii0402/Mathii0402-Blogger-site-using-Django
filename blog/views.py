from distutils.command.config import config
from django.shortcuts import render
from .models import post
from pickle import NONE
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

template_name: 'detailed.html'

def index(request):
    p=post.objects.all()
    return render(request, "index.html", {'post' : p}) 
  
def detailed(request):
    return render(request,'detailed.html')

 
def check(request):
    return render(request,"check.html")
# def register(request):

#     if request.method == 'POST':
#         firstname=request.POST['firstname']
#         secondname=request.POST['secondname']
#         username=request.POST['username']
#         password1=request.POST['pass1']
#         password2=request.POST['pass2']
#         email=request.POST['email']
        
        
#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'username taken!!!')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'email taken!!')
#                 return redirect('register')
#             else:    
#                 user = User.objects.create_user(username=username, password=password1, email=email, first_name=firstname, last_name=secondname )#creating object for saving in database
#                 user.save();
#                 messages.info(request,'user created!')
#                 return redirect('login')
                
               
#         else:
#             messages.info(request,"password didn't matched")
#             return redirect('register')
           
       
#     else:
#         return render(request,'register.html')

# def login(request):
#     if request.method=='POST':
#         username=request.POST['uname']
#         password=request.POST['passw']

#         use=auth.authenticate(username=username, password=password)
#         if use is not NONE:
#             auth.login(request,use)
#             return redirect('/')
#         else:
#             messages.error(request,'inlid credintials')
#             return redirect('login')
#     else:
#         return render(request,'login.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('/')
