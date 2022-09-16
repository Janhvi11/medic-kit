from ..forms import *
from ..models import *

from django.shortcuts import render, redirect, get_object_or_404


import logging
logger = logging.getLogger(__name__)



def viewTreatment(request):
    context = {}
    context["treatment"] = treatment.objects.all()
    return render(request, "treatmentview.html", context)

def addTreatment(request):
	context = {}
	form = RegisterTreatForm(request.POST)

	if form.is_valid():
			
			form.save()
			logger.info("Treatment was added")
			return redirect("/treatment/treatView/")

	context['form'] = form
	return render(request, "treatmentAdd.html",context)

def deleteTreatment(request,id):
	context={}
	obj = get_object_or_404(treatment, id=id)#
	if request.method == "GET":
		obj.delete()
		logger.info("Treatment was Deleted")

		return redirect("/treatment/treatView/")
	return render(request, "treatmentview.html", context)

def editTreatment(request,id):
    context = {}
    obj = get_object_or_404(treatment, id=id)
    form = RegisterTreatForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() #
		
        return redirect("/treatment/treatView/")
    
    context['form'] = form
    return render(request, "treatmentAdd.html",context)