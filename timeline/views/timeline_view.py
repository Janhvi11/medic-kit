from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from ..models import timeline, timeline_doc, timeline_pharma
from ..forms import timelineForm, timeline_pharmaForm, timeline_docForm
from django.utils import timezone
from register.models import user

#==================ADMIN==========================================
def viewAdminTime(request):
    context = {}
    # obj = get_object_or_404(ToDoItem, id=id)
    context = {"user":timeline.objects.all(), "doc":timeline_doc.objects.all(), "pharma": timeline_pharma.objects.all()}
    return render(request, "timeline-view.html", context)

#==================USER===========================================
def viewTime(request):
    context = {}
    username = request.session.get('username')
    # return HttpResponse(username)
    user_filter = user.objects.filter(username = username)
    # uid = user_filter[0]
    # uid = user_filter.first()
    uid = 1
    context["timeline"] = timeline.objects.filter(userId=uid)
    return render(request, "userside-view-time.html", context)

def addTime(request):
	context = {}
	form = timelineForm(request.POST)
	# form.cleaned_data['datetime'] = timezone.now()
	if form.is_valid():
			form.save()
			return redirect("/timeline/viewTimeline")

	context['form'] = form
	return render(request, "timelineAdd.html",context)

def deleteTime(request,id):
	context={}
	obj = get_object_or_404(timeline, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/timeline/viewTimeline/")
	return render(request, "timeline-view.html", context)

def editTime(request,id):
    context = {}    
    obj = get_object_or_404(timeline, id=id)
   
    form = timelineForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/timeline/viewTimeline/")
    
    context['form'] = form
    return render(request, "timelineAdd.html",context)

#============DOCTOR======================================================

def viewdocTime(request):
    context = {}
    # obj = get_object_or_404(ToDoItem, id=id)
    context["timeline"] = timeline_doc.objects.all()
    return render(request, "timeline-view.html", context)

def adddocTime(request):
	context = {}
	form = timeline_docForm(request.POST)
	# form.cleaned_data['datetime'] = timezone.now()
	if form.is_valid():
			form.save()
			return redirect("/timeline/viewTimeline")

	context['form'] = form
	return render(request, "timelineAdd.html",context)

def deletedocTime(request,id):
	context={}
	obj = get_object_or_404(timeline_doc, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/timeline/viewTimeline/")
	return render(request, "timeline-view.html", context)

def editdocTime(request,id):
    context = {}    
    obj = get_object_or_404(timeline_doc, id=id)
   
    form = timeline_docForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/timeline/viewTimeline/")
    
    context['form'] = form
    return render(request, "timelineAdd.html",context)

#============PHARMACIST======================================================

def viewpharmaTime(request):
    context = {}
    # obj = get_object_or_404(ToDoItem, id=id)
    context["timeline"] = timeline_pharma.objects.all()
    return render(request, "timeline-view.html", context)

def addpharmaTime(request):
	context = {}
	form = timeline_pharmaForm(request.POST)
	# form.cleaned_data['datetime'] = timezone.now()
	if form.is_valid():
			form.save()
			return redirect("/timeline/viewTimeline")

	context['form'] = form
	return render(request, "timelineAdd.html",context)

def deletepharmaTime(request,id):
	context={}
	obj = get_object_or_404(timeline_pharma, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/timeline/viewTimeline/")
	return render(request, "timeline-view.html", context)

def editpharmaTime(request,id):
    context = {}    
    obj = get_object_or_404(timeline_pharma, id=id)
   
    form = timeline_pharmaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/timeline/viewTimeline/")
    
    context['form'] = form
    return render(request, "timelineAdd.html",context)