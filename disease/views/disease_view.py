from ..forms import *
from ..models import *

from django.shortcuts import render, redirect, get_object_or_404

def viewDisease(request):
    context = {}
    context["disease"] = disease.objects.all()
    return render(request, "disease-view.html", context)