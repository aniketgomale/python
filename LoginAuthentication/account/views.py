from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def ahome(request):
    return render(request,'account/ahome.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('phome')

        else:
            return render(request, 'account/login.html', {'error': 'username or password is incorrect'})

    else:
        return render(request, 'account/login.html')


def signup(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['password1']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'account/signup.html',{'error':'Username is already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('ahome')
        else:
            return render(request, 'account/signup.html', {'error': 'password does not match'})
    else:
        return render(request,'account/signup.html')

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('ahome')