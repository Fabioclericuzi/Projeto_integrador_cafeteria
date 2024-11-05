from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def cardapio(request):
    return render(request, 'cardapio.html')

def contato(request):
    return render(request, 'contato.html')

def cadastro(request):
    return render(request, 'cadastro.html')