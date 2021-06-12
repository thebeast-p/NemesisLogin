from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from passlib.hash import pbkdf2_sha256

# Create your views here.
from django import forms


def login(request):
    return render (request, 'login.html', {'flag': False})

def signup(request):
    return render (request, 'signup.html')

def check(request):
    users= user.objects.all()
    mail= request.POST['uname']
    #x= request.POST['psw']
    #user1.psw= pbkdf2_sha256.encrypt(x,rounds=12000,salt_size=32)
    psw = request.POST['psw']
    
    for user1 in users:
        if mail in user1.mail and psw in user1.psw:
            return render (request, 'success.html')
    else:
        return render (request, 'login.html', {'flag': True})

def display(request):

    users= user.objects.all()

    #print (users)

    return render (request, 'data.html', {'user':users})