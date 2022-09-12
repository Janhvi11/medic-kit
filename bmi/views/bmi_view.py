from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from ..models import bmi, ideal_bmi
from ..forms import bmiForm, bmiIdealForm
from register.models import user

def viewbmi(request):
    context = {}
    context["bmi"] = bmi.objects.all()
    return render(request, ".html", context)

def addbmi(request):
	context = {}
	form = bmiForm(request.POST)
	# form.cleaned_data['datetime'] = timezone.now()
	if form.is_valid():
		form.save()
		return redirect("")

	context['form'] = form
	return render(request, ".html",context)

def deletebmi(request,id):
	context={}
	obj = get_object_or_404(bmi, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("")
	return render(request, ".html", context)

def editbmi(request,id):
    context = {}    
    obj = get_object_or_404(bmi, id=id)
   
    form = bmiForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("")
    
    context['form'] = form
    return render(request, ".html",context)