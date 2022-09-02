from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request,'about.html')

def news(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def buy(request):
    return render(request, 'buy.html')

def client(request):
    return render(request, 'client.html')

def contact(request):
    return render(request, 'contact.html')

def doctors(request):
    return render(request, 'doctors.html')

def index(request):
    return render(request, 'index.html')
