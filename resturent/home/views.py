from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def book(request):
    return render(request,'book.html')

def order(request):
    return render(request,'order.html')

def contact(request):
    return render(request,'contact.html')

def menu(request):
    return render(request,'menu.html')