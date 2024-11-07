from django.shortcuts import render
from django.contrib import messages
from .models import Contato
from django.utils import timezone

from .forms import ContatoForm


def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def cardapio(request):
    return render(request, 'cardapio.html')


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            Contato.objects.create(
                nome=form.cleaned_data['nome'],
                assunto=form.cleaned_data['assunto'],
                mensagem=form.cleaned_data['mensagem'],
                data_envio=timezone.now()
            )

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def cadastro(request):
    return render(request, 'cadastro.html')