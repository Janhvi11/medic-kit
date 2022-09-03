from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View

from ..forms import *
from ..models import *

def viewToDoList(request):
	context = {}
	context["todolist"] = ToDoList.objects.all()
	return render(request, "ToDoList-view.html", context)

def addToDoList(request):
	context = {}
	form = TodoListForm(request.POST)

	if form.is_valid():
			form.save()
			return redirect("/todo/viewToDoList")

	context['form'] = form
	return render(request, "ToDoListAdd.html",context)

def deleteToDoList(request,title):
	context={}
	obj = get_object_or_404(ToDoList, title=title)
	if request.method == "GET":
		obj.delete()
		return redirect("/todo/viewToDoList/")
	return render(request, "ToDoList-view.html", context)

def editToDoList(request,id):
    context = {}    
    obj = get_object_or_404(ToDoList, id=id)
   
    form = TodoListForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/todo/viewToDoList/")
    
    context['form'] = form
    return render(request, "ToDoListAdd.html",context)