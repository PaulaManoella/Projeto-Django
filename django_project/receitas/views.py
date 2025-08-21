from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    
    receitas = {
        1: 'lasanha',
        2: 'strogonoff',
        3: 'frango a milanesa',
        4: 'feijoada'   
    }
    
    dados_receitas={
        'nomes_receitas': receitas
    }
    
    # usando render para renderizar o arquivo html
    return render(request,
                  'index.html',
                #   passando context como parametro para renderizar na pagina html
                  dados_receitas)

def receita(request):
    return render(request,
                  'receita.html')