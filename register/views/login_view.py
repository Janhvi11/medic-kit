from tabnanny import check
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.views import LoginView #
from django.contrib.auth import authenticate, login
from ..models import user,doc,pharma
# from django.shortcuts import 
# from ..forms import LoginUserForm 
from ..forms import LoginUserForm, LoginDocForm, LoginPharmaForm

def login_home(request):
    return render(request, "login-main.html")

def login_request(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username_got = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            obj = get_object_or_404(user, username=username_got)
            res = check_password(password,obj.password1)            #check_password is an hashing method
            
            if res == True:
                # login(request, username_got)
                request.session['username']=form.cleaned_data.get('username')
                request.session['type']=0
                messages.info(request, f"You are now logged in as {username_got}")
      
                return redirect('/index/')

         
            else:
                messages.error(request, "Invalid username or password.")
                
    else:
        form = LoginUserForm()
        # messages.error(request, "error 2.")
    # form = AuthenticationForm()
    return render(request, template_name = "login.html", context = {"form":form})

def login_doc_request(request):
    # template_name = "login.html"
    # form_class = LoginUserForm
    if request.method == 'POST':
        form = LoginDocForm(request.POST)
        # form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username_got = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            #     # password = make_password(request.POST['password'])
            #     # return render(request, 'demo.html') #, {'access':check_password}
            
            obj = get_object_or_404(doc, username=username_got)
            res = check_password(password,obj.password)
            
            if res == True:
                request.session['type']=1
                request.session['username'] = form.cleaned_data.get('username')
                #request.session['type']=1
                # login(request, user_check)
                messages.info(request, f"You are now logged in as {username_got}")
                return HttpResponseRedirect('/index')
            else:
                messages.error(request, "Invalid username or password.")
                
    else:
        form = LoginDocForm()
        # messages.error(request, "error 2.")
    # form = AuthenticationForm()
    return render(request, template_name = "login.html", context = {"form":form})

def login_pharma_request(request):
    # template_name = "login.html"
    # form_class = LoginUserForm
    if request.method == 'POST':
        form = LoginPharmaForm(request.POST)
        # form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username_got = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            #     # password = make_password(request.POST['password'])
            #     # return render(request, 'demo.html') #, {'access':check_password}
            
            obj = get_object_or_404(pharma, username=username_got)
            res = check_password(password,obj.password)
            
            if res == True:
                request.session['type']=2
                request.session['username'] = form.cleaned_data.get('username')
                messages.info(request, f"You are now logged in as {username_got}")
                return HttpResponseRedirect('/index/')
            else:
                messages.error(request, "Invalid username or password.")
                
    else:
        form = LoginPharmaForm()
        # messages.error(request, "error 2.")
    # form = AuthenticationForm()
    return render(request, template_name = "login.html", context = {"form":form})

def logout(request):
    del request.session['type']
    del request.session['username']
    # except KeyError:
    #     pass
    return redirect('/index/')

# ============================PROFILES============================================================

def userprofile(request):
    return render(request, "user-profile.html")

def docprofile(request):
    return render(request, "doc-profile.html")

def pharmaprofile(request):
    return render(request, "pharma-profile.html")