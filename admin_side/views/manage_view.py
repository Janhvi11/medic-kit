from register.models import doc
from register.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password

def index_manage(req):
    return render(req, "login.html")

def viewDoc(request):
	context = {}
	context["doctor"] = doc.objects.all()
	return render(request, "doc-view.html", context)

def addDoc(request):
	context = {}
	form = RegisterDocForm(request.POST)

	if form.is_valid():
			sign_up = form.save(commit=False)
			sign_up.password = make_password(form.cleaned_data['password'])
			sign_up.save()
			return redirect("/ad/viewDoc")

	context['form'] = form
	return render(request, "docAdd.html",context)

def deleteDoc(request,username):
	context={}
	obj = get_object_or_404(doc, username=username)
	if request.method == "GET":
		obj.delete()
		return redirect("/ad/viewDoc/")
	return render(request, "doc-view.html", context)

def editDoc(request,username):
    context = {}
    obj = get_object_or_404(doc, username=username)
    form = RegisterDocForm(request.POST, instance=obj)
    if form.is_valid():
        sign_up = form.save(commit=False)
        sign_up.password = make_password(form.cleaned_data['password'])
        sign_up.save()
        return redirect("/ad/viewDoc/")
    
    context['form'] = form
    return render(request, "docAdd.html",context)
def viewPharma(request):
	context = {}
	context["pharmacists"] = pharma.objects.all()
	return render(request, "pharma-view.html", context)

def addPharma(request):
	context = {}
	form = RegisterPharmaForm(request.POST)
	
	if form.is_valid():
			sign_up = form.save(commit=False)
			sign_up.password = make_password(form.cleaned_data['password'])
			sign_up.save()
			return redirect("/ad/viewPharma/")

	context['form'] = form
	return render(request, "pharmaAdd.html",context)

def deletePharma(request,username):
	context={}
	obj = get_object_or_404(pharma, username=username)
	if request.method == "GET":
		obj.delete()
		return redirect("/ad/viewPharma/")
	return render(request, "pharma-view.html", context)

def editPharma(request,username):
    context = {}
    obj = get_object_or_404(pharma, username=username)
    form = RegisterPharmaForm(request.POST, instance=obj)
    if form.is_valid():
        sign_up = form.save(commit=False)
        sign_up.password = make_password(form.cleaned_data['password'])
        sign_up.save()
        return redirect("/ad/viewPharma/")
    
    context['form'] = form
    return render(request, "PharmaAdd.html",context)

