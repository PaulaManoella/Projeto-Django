from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # usando render para renderizar o arquivo html
    return render(request,
                  'index.html')

def receita(request):
    return render(request,
                  'receita.html')