from ..forms import *
from ..models import *

from django.shortcuts import render, redirect, get_object_or_404

def viewDisease(request):
    context = {}
    context["disease"] = disease.objects.all()
    return render(request, "diseaseview.html", context)

def addDisease(request):
	context = {}
	form = RegisterDisForm(request.POST)

	if form.is_valid():
			
			form.save()
			return redirect("ill/viewDisease/")

	context['form'] = form
	return render(request, "diseaseAdd.html",context)

def deleteDisease(request,id):
	context={}
	obj = get_object_or_404(disease, id=id)#
	if request.method == "GET":
		obj.delete()
		return redirect("ill/viewDisease/")
	return render(request, "diseaseview.html", context)

def editDisease(request,id):
    context = {}
    obj = get_object_or_404(disease, id=id)
    form = RegisterDisForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() #
        return redirect("ill/viewDoc/")
    
    context['form'] = form
    return render(request, "diseaseAdd.html",context)