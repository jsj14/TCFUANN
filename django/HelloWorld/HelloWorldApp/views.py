from django.shortcuts import render
from django.template import loader
from django.template import  Context,Template
from HelloWorldApp .normalisation_checkpoint import*
# Create your views here.
from django.http import HttpResponse 

def cover(request):
    template=loader.get_template("Cover.html")
    return HttpResponse(template.render())

def newpage(request):
    list_val=request.GET["list2"]
    
    template=loader.get_template("newpage.html")
    return HttpResponse(template.render())

def data(request):
    template=loader.get_template("withdata.html")
    return HttpResponse(template.render())

def graph(request):
    template=loader.get_template("graph2.html")
    '''list_val=request.GET["list2"]
    backend(list_val)'''
    return HttpResponse(template.render())

def maps(request):
    template=loader.get_template("mapindex1.html")
    return HttpResponse(template.render())

