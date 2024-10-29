from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
  
def index(request):
    return TemplateResponse(request,  "index.html")

def index(request):
    return TemplateResponse(request,  "feedback.html")

def index(request):
    return TemplateResponse(request,  "map.html")

def index(request):
    return TemplateResponse(request,  "with-a-hat-and-a-basement.html")



