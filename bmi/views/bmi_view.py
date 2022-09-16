from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from ..models import bmi, ideal_bmi
from ..forms import bmiForm, bmiIdealForm
from register.models import user

import logging
logger = logging.getLogger(__name__)


#===================================USER===========================================

def viewbmi(request):
    context = {}
    context["bmi"] = bmi.objects.all()
    return render(request, "bmi-view.html", context)

def addbmi(request):
	context = {}
	form = bmiForm(request.POST)
	# form.cleaned_data['datetime'] = timezone.now()
	if form.is_valid():
		form.save()
		logger.info("BMI was added")
		return redirect("/bmi/viewbmi/")

	context['form'] = form
	return render(request, "bmiAdd.html",context)

def deletebmi(request,id):
	context={}
	obj = get_object_or_404(bmi, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/bmi/viewbmi/")
	return render(request, "bmi-view.html", context)

def editbmi(request,id):
    context = {}    
    obj = get_object_or_404(bmi, id=id)
   
    form = bmiForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
		
        return redirect("/bmi/viewbmi/")
    
    context['form'] = form
    return render(request, "bmiAdd.html",context)

#===================================IDEAL===========================================

def viewidealbmi(request):
    context = {}
    context["ideal_bmi"] = ideal_bmi.objects.all()
    return render(request, "idealBmi-view.html", context)

def addidealbmi(request):
	context = {}
	form = bmiIdealForm(request.POST)
	# form.cleaned_data['datetime'] = timezone.now()
	if form.is_valid():
		form.save()
		return redirect("/bmi/viewidealbmi/")

	context['form'] = form
	return render(request, "idealBmiAdd.html",context)

def deleteidealbmi(request,id):
	context={}
	obj = get_object_or_404(ideal_bmi, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/bmi/viewidealbmi/")
	return render(request, "idealBmi-view.html", context)

def editidealbmi(request,id):
    context = {}    
    obj = get_object_or_404(ideal_bmi, id=id)
   
    form = bmiIdealForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/bmi/viewidealbmi/")
    
    context['form'] = form
    return render(request, "idealBmiAdd.html",context)