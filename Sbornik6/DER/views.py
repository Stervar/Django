from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from datetime import datetime

def current_datetime(request):
    now = datetime.now()
    return render(request, 'current_datetime.html', {'current_datetime': now})

