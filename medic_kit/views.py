from django.shortcuts import render,redirect
from django.http import HttpResponse
from appointment import *
from medic_kit.forms import AppointmentForm


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

# def addAppointment(request):
#     context = {}
#     form = AppointmentForm(request.POST)
    
#     if form.is_valid():
#         #return HttpResponse(form)
#         form.save()
#         return redirect("/index")

#     context['form'] = form
#     return render(request, "index.html",context)