from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View

from ..forms import *
from ..models import *


def viewNews(request):
	context = {}
	context["news"] = news.objects.all()
	return render(request, "news-view.html", context)

def deleteNews(request,id):
	context={}
	obj = get_object_or_404(news, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/newss/viewNews/")
	return render(request, "news-view.html", context)

#def addNews(request):
#    context = {}
#    form = NewsForm(request.POST)
#    
#    if form.is_valid():
#        # return HttpResponse(form)
#        if len(request.FILES) != 0:
#            form.image = request.FILES['image']
#        
#        form.save()
#        messages.success(request, "Blog added successfully")
#        return redirect("/index")
#
#    context['form'] = form
#    return render(request, "news/templates/news-add.html",context)


def addNews(request):

    form = NewsForm(request.POST,request.FILES)
    
    if form.is_valid():

        form.save()
        messages.success(request, "News Added Successfully")
        return redirect("/newss/viewNews/")
    
    return render(request, 'news-add.html')