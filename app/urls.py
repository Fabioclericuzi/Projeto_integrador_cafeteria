from django.urls import path

from .views import home, contato, cadastro, cardapio, sobre

urlpatterns = [
    path('', home, name='home'),
    path('cardapio', cardapio, name='cardapio'),
    path('contato', contato, name='contato'),
    path('cadastro', cadastro, name='cadastro'),
    path('sobre', sobre, name='sobre')
]