from django.shortcuts import render
from django.http import HttpResponse

def signup(request):
    return render(request,'signup.html')

def welcome(request):
    return render(request,'welcome.html')

def analyze(request):
        #Get the text
    userId      = request.GET.get('userId', 'off')
    userName    = request.GET.get('userName', 'off')
    userEmail   = request.GET.get('userEmail', 'off')
    userPass    = request.GET.get('userPass', 'off')
    regTime     = request.GET.get('regTime', 'off')

    return render(request, 'start.html')


