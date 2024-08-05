from django.db.models import Max, Min
from django.core.mail import send_mail


def filtrar_produtos(produtos, filtro):
    if filtro:
        if "-" in filtro:
            categoria, tipo = filtro.split("-")
            produtos = produtos.filter(tipo__slug=tipo, categoria__slug=categoria)
        else:
            produtos = produtos.filter(categoria__slug=filtro)
    return produtos

def preco_minimo_maximo(produtos):
    minimo = 0
    maximo = 0
    if len(produtos) > 0:
        maximo = list(produtos.aggregate(Max("preco")).values())[0]
        maximo = round(maximo, 2)
        minimo = list(produtos.aggregate(Min("preco")).values())[0]
        minimo = round(minimo, 2)
    return minimo, maximo

def ordenar_produtos(produtos, ordem):
    if ordem == "menor-preco":
        produtos = produtos.order_by("preco")
    elif ordem == "maior-preco":
        produtos = produtos.order_by("-preco")
    elif ordem == "mais-vendidos":
        produtos = list(produtos)  # Converte para uma lista
        produtos = sorted(produtos, key=lambda produto: produto.total_vendas(), reverse=True)
    return produtos

def enviar_email_compra(pedido):
    email = pedido.cliente.email
    assunto = f'Pedido Aprovado com Sucesso: {pedido.id}.'
    corpo = f'''Parabéns! Seu pedido foi aprovado.
    ID do pedido: {pedido.id}
    Valor Total: {pedido.preco_total}
    Quantidade de Produtos: {pedido.quantidade_total}'''
    remetente = 'weslleycorreapimenta2002@gmail.com'
    send_mail(assunto, corpo, remetente, [email])