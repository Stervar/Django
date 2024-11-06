from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

news = [
    {'id':1, 'title':'dsfgnhjsd1', 'text':'hgjkffdsbkjdhn1'},
    {'id':2, 'title':'dsfgnhjsd2', 'text':'hgjkffdsbkjdhn2'},
    {'id':3, 'title':'dsfgnhjsd3', 'text':'hgjkffdsbkjdhn3'},
    {'id':4, 'title':'dsfgnhjsd4', 'text':'hgjkffdsbkjdhn4'},
    {'id':5, 'title':'dsfgnhjsd5', 'text':'hgjkffdsbkjdhn5'},
    {'id':6, 'title':'dsfgnhjsd6', 'text':'hgjkffdsbkjdhn6'},
    {'id':7, 'title':'dsfgnhjsd7', 'text':'hgjkffdsbkjdhn7'},
]


def home(request):
    return render(request, 'home.html')

def newsPage(request, id=None):
    if not id:
        return render(request, 'news.html', {'news':news})
    else:
        return render(request, 'news.html', {'post':news[int(id)-1]})


def management(request, any_text=None):
    return render(request, 'management.html')

def history(request):
    return render(request, 'history.html')

def history_people(request):
    return render(request, 'history_people.html')

def history_photos(request):
    return render(request, 'history_photos.html')