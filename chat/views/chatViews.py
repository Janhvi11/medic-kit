from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from ..models import chat
from ..forms import chatForm
from register.models import user
import csv

def chatView(request):
    context = {}
    
    username = request.session.get('username')
    context['username'] = username
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    data = chat.objects.all()
    context['chat'] = data
    
    return render(request,"chatView.html",context)

def chatAdd(request):
    context = {}
    form = chatForm(request.POST)
	# form.cleaned_data['datetime'] = timezone.now()
    if form.is_valid():
        form.save()
		# logger.info("BMI was added")
        return redirect("/chat/viewChat/")

    context['form'] = form
    return render(request, "chatAdd.html",context)

def chatDelete(request,id):
	context={}
	obj = get_object_or_404(chat, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/chat/viewChat/")
	return render(request, "chatView.html", context)

def chatEdit(request,id):
    context={}   
    obj = get_object_or_404(chat, id=id)
   
    form = chatForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
		
        return redirect("/chat/viewChat/")
    
    context['form'] = form
    return render(request, "chatAdd.html",context)