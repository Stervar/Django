"""
URL configuration for Sbornik6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DER import views
from django.views.generic import TemplateView
from django.urls import path, include
from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from DER import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # главная страница
    path('news/', views.newsPage, name='newsPage'),  # страница новостей
    path('news/<str:any_text>/', views.newsPage, name='news_with_text'),  # любой текст после news/
    path('management/', views.management, name='management'),  # страница руководства
    path('management/<str:any_text>/', views.management, name='management_with_text'),  # любой текст после management/
    path('history/', views.history, name='history'),
    path('history/people/', views.history_people, name='history_people'),
    path('history/photos/', views.history_photos, name='history_photos'),
]
