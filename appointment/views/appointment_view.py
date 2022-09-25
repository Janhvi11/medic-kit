import csv
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View

from ..models import *
from ..forms import *

import logging
logger = logging.getLogger(__name__)
#logger = logging.getLogger('django')

def viewAppointment(request):
    context = {}
    context["appointment"] = Appointment.objects.all()
    logger.info("Appointment has been viewed")
    return render(request, "appointment-view.html", context)

def deleteAppointment(request,id):
	context={}
	obj = get_object_or_404(Appointment, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/appointment/viewuserappointment/")
	return render(request, "user-side-appointment.html", context)

def addAppointment_UserProfile(request):
    context = {}
    form = UserAppointmentForm(request.POST)
    username = request.session.get('username')
    context['user_username'] = username
    if form.is_valid():
        #return HttpResponse(form)
        form.save()
        logger.info("User appointment has been added")
        return redirect("/appointment/viewuserappointment/")

    context['form_user'] = form
    return render(request, "user-side-appointment-add.html", context)

# index page view:
def addAppointmentUser(request):
    context = {}
    form = UserAppointmentForm(request.POST)
    username = request.session.get('username')
    context['user_username'] = username
    if form.is_valid():
        #return HttpResponse(form)
        form.save()
        logger.info("User appointment has been added")
        return redirect("/index/")

    context['form_user'] = form
    return render(request, "index.html", context)


def viewAppointment_UserSide(request):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    context['data'] = Appointment.objects.all()
    logger.info("Appointment has been viewed")
    return render(request, "user-side-appointment.html", context)

# profile page view:
def addAppointment_UserSide(request):
    context = {}
    form = UserAppointmentForm(request.POST)
    
    if form.is_valid():
        #return HttpResponse(form)
        form.save()
        logger.info("User appointment has been added")
        return redirect("/doctors/")

    context['form_user'] = form
    return render(request, "doctors.html", context)

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

# fname = models.CharField(max_length=100)
#     lname = models.CharField(max_length=100)
#     email = models.EmailField()
#     address = models.CharField(max_length=200)
#     time = models.CharField(max_length=500,choices=time)
#     day = models.CharField(max_length=500,choices=day)
#     request = models.TextField(max_length=500)
#     status = models.CharField(max_length=500,choices=status,default='Pending')
#     doctorId = models.IntegerField(null=True,default=0)

def download_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=disease.csv'
	writer = csv.writer(response)
	writer.writerow(['First Name','Last Name','Email','Address','Time','Day','Request','Status','Doctor Id'])
	for data in Appointment.objects.all():
		writer.writerow([data.fname,data.lname,data.email,data.address,data.time,data.day,data.request,data.status,data.doctorId])

	return response