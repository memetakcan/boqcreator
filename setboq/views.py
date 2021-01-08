from django.shortcuts import get_object_or_404,HttpResponseRedirect,redirect,Http404,render
from setboq.models import *
from .forms import SetboqForm
from .forms import GetboqForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import string
import sqlite3
from .dbmodel import *

abc = string.ascii_lowercase

def set_boq(request):

    if request.user.is_authenticated:
        form = SetboqForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            #-------------------------------------------------------------#
            loc = "C:\\Users\\Mehmet.BOLD\\Desktop\\BOQ\\db.sqlite3"
            con = sqlite3.connect(loc)
            cursor = con.cursor()
            cursor.execute("SELECT*FROM setboq_setboq")
            data = cursor.fetchall()
            db_boqdes = []
            db_boqcodes = []
            for i in data:
                if i[8] == form.cleaned_data.get("project"):
                    db_boqdes.append(i[5])
                    db_boqcodes.append(i[10])
            # ------------------------------------------------------------#
            if form.cleaned_data.get("boqcodes") in db_boqcodes:
                messages.warning(request,"Another BIM Object has this BoQ Codes")
            else:
                a.save()
                messages.success(request, "Successful Creation")
                return HttpResponseRedirect(a.get_absolute_url())
        context = {"form": form}
        return render(request,"getsetboq/form.html", context)
    else:
        return Http404()

def delete_boq(request,id):
    if request.user.is_authenticated:
        a = get_object_or_404(setboq, id=id)
        a.delete()
        return redirect("setboq:index")
    else:
        return Http404()

def index_boq(request):
    a_list = setboq.objects.all()
    query = request.GET.get("q")
    if query:
        a_list = a_list.filter(
            Q(boqdescription__icontains=query) |
            Q(boqcodes__icontains=query)
        ).distinct()

    paginator = Paginator(a_list, 15) # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        a = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        a = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        a = paginator.page(paginator.num_pages)


    return render(request, "getsetboq/index.html", {"r": a})

def update_boq(request,id):
    if request.user.is_authenticated:
        a = get_object_or_404(setboq,id=id)
        form = SetboqForm(request.POST or None,request.FILES or None,instance=a)
        if form.is_valid():
            form.save()
            messages.success(request, "Başarılı bir şekilde BOQ güncellendi.")
            return HttpResponseRedirect(a.get_absolute_url())
        context = {"form": form}
        return render(request,"getsetboq/form.html", context)
    else:
        return Http404()
def detail_boq(request,id):
    a = get_object_or_404(setboq,id=id)
    context = {"i": a}
    return render(request, "getsetboq/detail.html", context)

def get_boq(request):
    a_list = setboq.objects.all()
    if request.user.is_authenticated:
        form = GetboqForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            c = form.cleaned_data.get("category")
            m = form.cleaned_data.get("material")
            t = form.cleaned_data.get("schtype")

            if form.cleaned_data.get("objecttype") == "Family" and form.cleaned_data.get("schedulein") == "1":
                s = "2"
            elif form.cleaned_data.get("objecttype") == "Material" and form.cleaned_data.get("schedulein") == "1":
                s = "1"
            elif form.cleaned_data.get("objecttype") == "Material" and form.cleaned_data.get("schedulein") == "0":
                s = "4"
            else:
                s = "3"

            boq_code = str(c)+str(m)+str(abc[0])+str(s)+str(t)
            a.boqcodes = boq_code
            #-------------------------------------------------------------#
            loc = "C:\\Users\\Mehmet.BOLD\\Desktop\\BOQ\\db.sqlite3"
            con = sqlite3.connect(loc)
            cursor = con.cursor()
            cursor.execute("SELECT*FROM setboq_setboq")
            data = cursor.fetchall()
            db_boqdes = []
            db_boqcodes = []
            for i in data:
                if i[8] == form.cleaned_data.get("project"):
                    db_boqdes.append(i[5])
                    db_boqcodes.append(i[10])
            # ------------------------------------------------------------#
            k = 1
            while True:
                if boq_code in db_boqcodes:
                    boq_code = str(c)+str(m)+str(abc[k])+str(s)+str(t)
                    k = k+1
                else:
                    a.boqcodes = boq_code
                    break
            if form.cleaned_data.get("boqdescription") in db_boqdes:
                messages.warning(request,"Another BIM Object has this BoQ Description ")
            else:
                a.save()
                messages.success(request, "Successful Creation")
                return HttpResponseRedirect(a.get_absolute_url())
        context = {"form": form}
        return render(request,"getsetboq/form.html", context)
    else:
        return Http404()