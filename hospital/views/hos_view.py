from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View

from ..forms import *
from ..models import *


import logging
logger = logging.getLogger(__name__)


def viewhos(request):
	context = {}
	context["hos"] = hos.objects.all()
	return render(request, "hos-view.html", context)

def addhos(request):
    context = {}
    form = hospitalForm(request.POST or None)
    
    if form.is_valid():
        # return HttpResponse(form)
        form.save()
        logger.info("Hospital Information was added")
        return redirect("/hospital/viewHos")

    context['form'] = form
    return render(request, "hosAdd.html",context)

def deletehos(request,id):
	context={}
	obj = get_object_or_404(hos, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/hospital/viewHos/")
	return render(request, "hos-view.html", context)

def edithos(request,id):
    context = {}    
    obj = get_object_or_404(hos, id=id)
   
    form = hospitalForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        logger.info("Hospital Information was Edited")
        return redirect("/hospital/viewHos/")
    
    context['form'] = form
    return render(request, "hosAdd.html",context)