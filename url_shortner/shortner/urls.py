from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:uuid>', views.return_orginal_url, name='return_orginal_url')
]
