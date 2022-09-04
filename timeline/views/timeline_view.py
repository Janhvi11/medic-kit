from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from ..models import timeline
from ..forms import timelineForm
from django.utils import timezone

def viewTime(request):
    context = {}
    # obj = get_object_or_404(ToDoItem, id=id)
    context["timeline"] = timeline.objects.all()
    return render(request, "timeline-view.html", context)

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