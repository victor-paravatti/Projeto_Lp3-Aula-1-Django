from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from random import randint


def home(request):
    jogos = []
    repeticoes = []
    if request.POST:
        n = int(request.POST['variavel'])
        for i in range(n):
            jogo = []
            count = 0
            while(count < 15):
                numero = randint(1, 25)
                if numero not in jogo:
                    jogo.append(numero)
                    count += 1
            jogos.append(jogo)
        
        for i in range(1, 26):
            count = 0
            for j in jogos:
                if i in j:
                    count += 1
            repeticoes.append(count)
    contexto = {'jogos': jogos, 'repeticoes': repeticoes }   
    return render(request,'home.html', contexto)

