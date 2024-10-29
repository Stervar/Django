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
from django.urls import path
from django.views.generic import TemplateView
 
urlpatterns = [
    path("with-a-hat-and-a-basement/", TemplateView.as_view(template_name="with-a-hat-and-a-basement.html")),
    path("map/", TemplateView.as_view(template_name="map.html")),
    path("index/", TemplateView.as_view(template_name="index.html")),
    path("feedback/", TemplateView.as_view(template_name="feedback.html")),
]
