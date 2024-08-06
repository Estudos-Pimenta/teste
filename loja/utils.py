from django.db.models import Max, Min
from django.core.mail import send_mail
from django.http import HttpResponse
import csv

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
        lista_produtos = []
        for produto in produtos:
            lista_produtos.append((produto.total_vendas(), produto))
        lista_produtos = sorted(lista_produtos, reverse=True, key=lambda tupla: tupla[0])
        produtos = [item[1] for item in lista_produtos]
    return produtos

def enviar_email_compra(pedido):
    email = pedido.cliente.email
    assunto = f"Pedido aprovado: {pedido.id}"
    corpo = f"""Parabéns! Seu pedido foi aprovado.
    ID do pedido: {pedido.id}
    Valor total: {pedido.preco_total}
    Quantidade de produtos: {pedido.quantidade_total}"""
    remetente = "pythonimpressionador@gmail.com"
    send_mail(assunto, corpo, remetente, [email])

def exportar_csv(informacoes):
    # print(informacoes.model)
    colunas = informacoes.model._meta.fields
    nomes_colunas = [coluna.name for coluna in colunas]
    
    resposta = HttpResponse(content_type="text/csv")
    resposta["Content-Disposition"] = "attachment; filename=export.csv"
    
    criador_csv = csv.writer(resposta, delimiter=";")
    
    criador_csv.writerow(nomes_colunas)
    # escrever as linhas do csv
    for linha in informacoes.values_list():
        criador_csv.writerow(linha)
    return resposta