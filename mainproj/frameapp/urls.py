from django.contrib import admin
from django.urls import path
from . import views
from mainapp import views as mainapp_views

urlpatterns = [
	path('', mainapp_views.mypage, name='mypage'),
    path('text/', views.text, name='text'),
    path('background/', views.background, name='background'),
]  
    