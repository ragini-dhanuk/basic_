from django.urls import path
from . import views # from current folder import view.py
urlpatterns =[path('',view=views.landing, name='landing')],