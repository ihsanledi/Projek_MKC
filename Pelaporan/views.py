from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Main(request):

    return render(request, 'index.html')


def Login(request):
    return render(request, 'Login.html')


def Signin(request):
    return render(request, 'Signin.html')






