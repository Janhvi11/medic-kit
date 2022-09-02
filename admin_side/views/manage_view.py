from django.shortcuts import render
from register.models import doc
from register.forms import *
from django.shortcuts import render, redirect, get_object_or_404

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
		form.save()
		return redirect("/ad/viewDoc/")

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
        form.save()
        return redirect("/ad/viewDoc/")
    
    context['form'] = form
    return render(request, "docAdd.html",context)