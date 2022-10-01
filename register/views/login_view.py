
import os
import re
import statistics
from tabnanny import check
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.views import LoginView #
from django.contrib.auth import authenticate, login
from django.conf import settings
from medic_kit.settings import PROJECT_ROOT
from ..models import user,doc,pharma
import io
import numpy as np
from PIL import Image
import face_recognition
# from django.shortcuts import 
# from ..forms import LoginUserForm 
from ..forms import LoginUserForm, LoginDocForm, LoginPharmaForm
import cv2
import base64
from django.core.files.base import ContentFile
from django.templatetags.static import static
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

# ======================================================================================================

def view_doctors(request):
    context = {}
    context['data'] = doc.objects.all()
    
    return render(request,'user-side-doctor-view.html', context)


def video(request):
    return render(request,'video.html')


def base64_file(request,data):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    name = 'Demo'
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))

def base64_file_image(request):
    data=request.POST.get('dataimg')
    encoded_img = data.split(",")[1]
    # return HttpResponse(encoded_img)
    binary = base64.b64decode(encoded_img)
    image = np.asarray(bytearray(binary), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    face_locations = face_recognition.face_locations(image)
    enterimage_encoding = face_recognition.face_encodings(image)[0]
    results = face_recognition.compare_faces([enterimage_encoding], enterimage_encoding)
    users=user.objects.all()
    for u in users:
        d=os.path.join(settings.PROJECT_ROOT, u.image.url)
        # demo=static('img/blog/blog_1.jpg')
        # prefix = 'https://' if request.is_secure() else 'http://'
        image_url ='../../../..'+u.image.url
        img = Image.open(static('img/blog/blog_1.jpg'))
 
# asarray() class is used to convert
# PIL images into NumPy arrays
        numpydata = np.asarray(img)
        return HttpResponse(numpydata)
    return HttpResponse(results)
