from django.shortcuts import render,HttpResponse
from getboq.models import *
from setboq.models import *
# Create your views here.

def get_boq(request):
    a = setboq.objects.all()
    return render(request, "getsetboq/getboq.html", {"r": a})

def delete_boq(request):
    return HttpResponse("delete_boq")

def index_boq(request):
    a = getboq.objects.all()
    return HttpResponse("index_boq")

def update_boq(request):
    return HttpResponse("update_boq")

def detail_boq(request):
    return HttpResponse("detail_boq")