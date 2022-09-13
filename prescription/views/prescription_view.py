from ..forms import *
from ..models import *

from django.shortcuts import render, redirect, get_object_or_404

def viewPrescription(request):
    context = {}
    context["prescription"] = prescription.objects.all()
    return render(request, "prescriptionview.html", context)

def addPrescription(request):
	context = {}
	form = RegisterPrescriptionForm(request.POST)

	if form.is_valid():
			
			form.save()
			return redirect("/prescription/prescriptionView/")

	context['form'] = form
	return render(request, "prescriptionAdd.html",context)

def deletePrescription(request,id):
	context={}
	obj = get_object_or_404(prescription, id=id)#
	if request.method == "GET":
		obj.delete()
		return redirect("/prescription/prescriptionView/")
	return render(request, "prescriptionview.html", context)

def editPrescription(request,id):
    context = {}
    obj = get_object_or_404(prescription, id=id)
    form = RegisterPrescriptionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() #
        return redirect("/prescription/prescriptionView/")
    
    context['form'] = form
    return render(request, "prescriptionAdd.html",context)