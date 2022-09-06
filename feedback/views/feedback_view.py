from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View

from ..forms import *
from ..models import *

def viewFeedback(request):
	context = {}
	context["feedback"] = feedback.objects.all()
	return render(request, "feedback-view.html", context)

def deleteFeedback(request,id):
	context={}
	obj = get_object_or_404(feedback, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/feedback/viewFeedback/")
	return render(request, "feedback-view.html", context)

def addFeedback(request):
    context = {}
    form = FeedbackForm(request.POST)
    
    if form.is_valid():
        # return HttpResponse(form)
        form.save()
        return redirect("/index")

    context['form'] = form
    return render(request, "feedback.html",context)

def user_addFeedback(request):
    context = {}
    form = FeedbackForm(request.POST)
    
    if form.is_valid():
        # return HttpResponse(form)
        form.save()
        return redirect("/index")

    context['form'] = form
    return render(request, "user_feedback.html",context)