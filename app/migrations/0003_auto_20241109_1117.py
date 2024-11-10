from django.db import migrations

def insert_initial_data(apps, schema_editor):
    Estoque = apps.get_model('app', 'Estoque')

    produtos = [
        ('Café Expresso', 50, 7.00),
        ('Café Brasileiro', 50, 9.00),
        ('Cappuccino', 50, 12.00),
        ('Latte', 50, 12.00),
        ('Flat White', 50, 13.00),
        ('Mocha', 50, 10.00),
        ('Affogato', 50, 18.00),
        ('Café Gelado', 50, 9.00),
        ('Chá de Hortelã', 50, 12.00),
        ('Chá de Camomila', 50, 10.00),
        ('Chá de Hortelã', 50, 10.00),
        ('Chá Verde', 50, 8.00),
        ('Smoothie de Frutas Vermelhas', 50, 17.00),
        ('Milkshake de Baunilha ou Chocolate', 50, 15.00),
        ('Limonada Siciliana', 50, 15.00),
        ('Irish Coffee', 50, 20.00),
        ('Croissant de Manteiga', 50, 13.00),
        ('Croissant de Chocolate', 50, 13.00),
        ('Pão de Queijo', 50, 8.00),
        ('Brioche', 50, 9.00),
        ('Coxinha', 50, 10.00),
        ('Sanduíche Crocante de Presunto e Queijo', 50, 12.00),
        ('Panini de Frango e Queijo', 50, 12.00),
        ('Cheesecake de Frutas Vermelhas', 50, 13.00),
        ('Pavê de Chocolate', 50, 13.00),
        ('Mousse de Maracujá', 50, 12.00),
        ('Brownie de Chocolate', 50, 13.00),
        ('Torta de Limão', 50, 13.00),
        ('Panqueca', 1, 13.00),
    ]

    for produto in produtos:
        if not Estoque.objects.filter(produto_nome=produto[0]).exists():
            Estoque.objects.create(produto_nome=produto[0], quantidade_disponivel=produto[1], preco_unitario=produto[2])

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_pedido_itempedido'),
    ]

    operations = [
        migrations.RunPython(insert_initial_data),
    ]
