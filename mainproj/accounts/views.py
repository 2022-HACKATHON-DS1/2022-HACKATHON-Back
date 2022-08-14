from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == "POST":
        if request.POST.get('PASSWORD')==request.POST.get('Confirm PW'):
            user=User.objects.create_user(request.POST.get('username'), password=request.POST.get('PASSWORD'))
            auth.login(request,user)

            return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('PASSWORD', None)
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'login.html')
    
def home(request):
    return render(request, 'home.html')