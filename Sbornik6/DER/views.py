from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from datetime import datetime

def current_datetime(request):
    now = datetime.now()
    return render(request, 'current_datetime.html', {'current_datetime': now})


from django.shortcuts import render

def multiplication_table(request):
    table = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return render(request, 'multiplication_table.html', {'table': table})