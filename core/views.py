from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from random import randint


def home(request):
    jogos = []

    if request.POST:
        n = int(request.POST['variavel'])
        for j in range(n):
            jogo = []
            for i in range(10):
                jogo.append((randint(1, 25)))
            jogos.append(jogo)
    
    contexto = {'jogos': jogos}   
    return render(request,'home.html', contexto)

