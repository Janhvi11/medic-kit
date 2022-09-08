from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request,'about.html')

def news(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:    
        return render(request, 'news.html')

def blog(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'blog.html')

def buy(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'buy.html')

def client(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'client.html')

def contact(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'contact.html')

def feedback(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'feedback.html')

def doctors(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'doctors.html')

def index(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'index.html')