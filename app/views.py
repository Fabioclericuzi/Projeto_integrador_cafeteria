from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Contato
from .forms import ContatoForm, UsuarioForm
from .models import Estoque
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Pedido, ItemPedido, Usuario
import json

def validate_user(request):
    cpf = request.GET.get('cpf')
    user_exists = Usuario.objects.filter(cpf=cpf).exists()
    return JsonResponse({'valid': user_exists})


def home(request):
    return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')


def cardapio(request):
    produtos = Estoque.objects.all()
    return render(request, 'cardapio.html', {'produtos': produtos})


def contato(request):
    form = ContatoForm(request.POST or None)

    if request.method == 'POST':
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
    form = UsuarioForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('cadastro')
        else:
            messages.error(request, 'Erro ao cadastrar usuário')

    context = {
        'form': form
    }
    return render(request, 'cadastro.html', context)


@csrf_exempt
def finalize_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cpf = data.get('cpf')
        items = data.get('items')
        total = data.get('total')

        try:
            usuario = Usuario.objects.get(cpf=cpf)
        except Usuario.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Usuário não encontrado.'})

        pedido = Pedido.objects.create(usuario=usuario, total=total)

        for item in items:
            nome_produto = item.get('name')
            preco = item.get('price')

            ItemPedido.objects.create(pedido=pedido, nome_produto=nome_produto, preco=preco)

        return JsonResponse({
            'success': True,
            'total': total,
            'items': [{'nome_produto': item.get('name')} for item in items]
        })

