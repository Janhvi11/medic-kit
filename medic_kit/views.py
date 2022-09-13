from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from register.models import user
from django.contrib.auth.hashers import make_password
from register.forms import RegisterForm
# from django.shortcuts import render, redirect, ,HttpResponse


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
    
def userProfile(request):
    context={}
    type= request.session.get('type')
    uname = request.session.get('username')
    context['username'] = uname
    
    # form : view and update:
    
    context['users'] = user.objects.filter(username=uname)
	# obj = get_object_or_404(user, username=uname)
    
    
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'user-profile.html',context)
    
def edituserProfile(request,id):
    context_3 = {}
    obj = get_object_or_404(user, id=id)
    form = RegisterForm(request.POST or None, instance=obj)
    if form.is_valid():
        sign_up = form.save(commit=False)
        sign_up.password1 = make_password(form.cleaned_data['password1'])
        request.session['username'] = form.cleaned_data['username']
        sign_up.save()
        return redirect("/userProfile/")
    
    context_3['form'] = form
    return render(request, "edit-user-profile.html",context_3)