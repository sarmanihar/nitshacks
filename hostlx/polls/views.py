"""from tkinter import N
from django.shortcuts import render
from django.http import HttpResponse
from .models import signup, table, orders
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
# Create your views here.
# username1=''
# usename=username1+User_name

username1 = ''


def signup1(request):
    if request.method == 'POST':
        if request.POST.get('User_name') and request.POST.get('First_name') and request.POST.get('Last_name') and request.POST.get('Email_id') and request.POST.get('Password') and request.POST.get('city') and request.POST.get('country') and request.POST.get('state') and request.POST.get('profession'):
            post = signup()

            post.User_name = request.POST.get('User_name')

            global username1
            username1 = username1 + request.POST.get('User_name')

            post.First_name = request.POST.get('First_name')
            post.Last_name = request.POST.get('Last_name')
            post.Email_id = request.POST.get('Email_id')
            post.Password = request.POST.get('Password')
            post.city = request.POST.get('city')
            post.country = request.POST.get('country')
            post.state = request.POST.get('state')
            post.profession = request.POST.get('profession')
            post.save()
            print(username1)
            # print(request.POST.get('First_name'))
            #success='your account has been created...'
            # return HttpResponse(success)
            return render(request, 'home2.html')
    else:
        return render(request, 'b.html')
        """
from django.shortcuts import render  

def home(request):
    return render(request, 'test.html')  