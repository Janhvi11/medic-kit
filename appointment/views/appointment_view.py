from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View

from ..models import *
from ..forms import *

def viewAppointment(request):
    context = {}
    context["appointment"] = Appointment.objects.all()
    return render(request, "appointment-view.html", context)

def deleteAppointment(request,id):
	context={}
	obj = get_object_or_404(Appointment, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/appointment/viewappointment/")
	return render(request, "appointment-view.html", context)

def addAppointment(request):
    context = {}
    form = AppointmentForm(request.POST)
    
    if form.is_valid():
        #return HttpResponse(form)
        form.save()
        return redirect("/appointment/viewappointment")

    context['form'] = form
    return render(request, "appointment-add.html",context)

#def acceptappointment(request):
#    context = {}
#    form = AcceptAppointmentForm(request.POST)
#    
#    if form.is_valid():
#        # return HttpResponse(form)
#        form.save()
#        return redirect("/appointment/viewappointment")
#
#    context['form'] = form
#    return render(request, "appointment-accept.html",context)