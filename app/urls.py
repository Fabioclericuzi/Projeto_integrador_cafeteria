from django.urls import path
from . import views

from .views import home, contato, cadastro, cardapio, sobre

urlpatterns = [
    path('', home, name='home'),
    path('cardapio', cardapio, name='cardapio'),
    path('contato', contato, name='contato'),
    path('cadastro', cadastro, name='cadastro'),
    path('sobre', sobre, name='sobre'),
    path('validate-user', views.validate_user, name='validate-user'),
    path('finalize-order/', views.finalize_order, name='finalize_order')
]