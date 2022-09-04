from ..forms import *
from ..models import *

from django.shortcuts import render, redirect, get_object_or_404

def viewMedhistory(request):
    context = {}
    context["medhistory"] = medhistory.objects.all()
    return render(request, "medhistoryview.html", context)

def addMedhistory(request):
	context = {}
	form = RegisterMedhistoryForm(request.POST)

	if form.is_valid():
			
			form.save()
			return redirect("/medhistory/medhistoryView/")

	context['form'] = form
	return render(request, "medhistoryAdd.html",context)

def deleteMedhistory(request,id):
	context={}
	obj = get_object_or_404(medhistory, id=id)#
	if request.method == "GET":
		obj.delete()
		return redirect("/medhistory/medhistoryView/")
	return render(request, "medhistoryview.html", context)

def editMedhistory(request,id):
    context = {}
    obj = get_object_or_404(medhistory, id=id)
    form = RegisterMedhistoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() #
        return redirect("/medhistory/medhistoryView/")
    
    context['form'] = form
    return render(request, "MedhistoryAdd.html",context)