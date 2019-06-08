from django.urls import path

from . import views

urlpatterns = [
    path('home', views.dio, name='home'),
    path('about', views.about, name='about'),
    path('thanks', views.thanks, name='thanks'),
    path('zakaz', views.zakaz, name='zakaz'),
]