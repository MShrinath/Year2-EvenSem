from django.shortcuts import render ,redirect
from .models import User
from django.db.models import Q

def HomePage(request):
    return render(request, 'index.html')

def LoginPage(request):
    return render(request, 'login.html')

def SignupPage(request):
    return render(request, 'signup.html')

def ls(request):
    return render(request, 'success.html')

def lf(request):
    return render(request, 'fail.html')


def LoginUser(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        flag = User.objects.filter(Q(username=uname, password=pwd)).values() 
        if flag:
            return redirect('ls')
        else:
            return redirect('lf')
        
def SignupUser(request):
    if request.method == "POST":
        name = request.POST["name"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        User.objects.create(name=name, username=uname, password=pwd)
        return redirect('loginPage')
    return render(request, 'signup.html')