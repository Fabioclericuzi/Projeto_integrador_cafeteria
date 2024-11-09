from django.contrib import admin
from .models import Estoque

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto_nome', 'quantidade_disponivel', 'preco_unitario')
    search_fields = ('produto_nome',)
    list_filter = ('quantidade_disponivel',)


