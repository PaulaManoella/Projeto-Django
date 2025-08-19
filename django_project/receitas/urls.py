# importando urls
from django.urls import path

# importando views
from . import views

urlpatterns=[
    path('', views.index, name='index')
]