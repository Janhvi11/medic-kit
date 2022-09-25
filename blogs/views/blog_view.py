from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from ..forms import *
from ..models import *


import logging
logger = logging.getLogger(__name__)

def viewBlog(request):
	context = {}
	context["blogs"] = blog.objects.all()
	return render(request, "blogs-view.html", context)

def deleteBlog(request,id):
	context={}
	obj = get_object_or_404(blog, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/newss/viewBlog/")
	return render(request, "blogs-view.html", context)

#def addBlog(request):
#    context = {}
#    form = BlogForm(request.POST)
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
#    return render(request, "news/templates/blog-add.html",context)




def addBlog(request):

    form = BlogForm(request.POST,request.FILES)
          
    if form.is_valid():

        form.save()
        logger.info("Blog was added")

        messages.success(request, "Blog Added Successfully")
        return redirect("/blogss/viewBlog/")
    
    return render(request, 'blogs-add.html')