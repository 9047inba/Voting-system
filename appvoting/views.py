from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from appvoting.models import *

# Create your views here.

def main(request):
    return render(request,'home.html')

def admin(request):
    return render(request,'adminpass.html')

def adminlogin(request):
    return render(request,'admin.html')

    # form = adminlogin()

    # if request.method=='POST':
    #     form = adminlogin(render.POST)

    #     if form.is_valid():


        


def voterlogin(request):
    return render(request,'voter.html')

