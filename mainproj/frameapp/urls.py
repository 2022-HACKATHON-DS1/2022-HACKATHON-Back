from django.contrib import admin
from django.urls import path
from . import views
from mainapp import views as mainapp_views

urlpatterns = [
	path('', mainapp_views.detail, name="detail"),
    path('text/', views.text, name='text'),
    path('text/background/', views.background, name='background'),
]  
    