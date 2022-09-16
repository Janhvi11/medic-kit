from ..forms import *
from ..models import *

from django.shortcuts import render, redirect, get_object_or_404

import logging
logger = logging.getLogger(__name__)

def viewDisease(request):
    context = {}
    context["disease"] = disease.objects.all()
    return render(request, "diseaseview.html", context)

def addDisease(request):
	context = {}
	form = RegisterDisForm(request.POST)

	if form.is_valid():
			
			form.save()
			logger.info("Diesease was added")
			return redirect("/ill/diseaseView/")

	context['form'] = form
	return render(request, "diseaseAdd.html",context)

def deleteDisease(request,id):
	context={}
	obj = get_object_or_404(disease, id=id)#
	if request.method == "GET":
		obj.delete()
		logger.info("Disease was Deleted")
		return redirect("/ill/diseaseView/")
	return render(request, "diseaseview.html", context)

def editDisease(request,id):
    context = {}
    obj = get_object_or_404(disease, id=id)
    form = RegisterDisForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() #
		
        return redirect("/ill/diseaseView/")
    
    context['form'] = form
    return render(request, "diseaseAdd.html",context)