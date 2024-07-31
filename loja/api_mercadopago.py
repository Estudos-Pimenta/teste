import mercadopago
public_key =  "APP_USR-dd7b7825-e3d3-47ad-b582-2836ac155d14"
token = "APP_USR-7769193582522514-073017-6a1a4bf4137e959cda95b77b38fea67c-1925206522"

def criar_pagamento(itens_pedido, link):
    sdk = mercadopago.SDK(token)
    #itens que ele esta comprando no formato de um dicionário
    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.item_estoque.produto.nome
        preco_unitario = float(item.item_estoque.produto.preco)
        itens.append({
            "title": nome_produto,
            "quantity": quantidade,
            "unit_price": preco_unitario,
        })

    #valor total
    preference_data = {
        "items": itens,
        "back_urls":{
            "success": link,
            "pending": link,
            "failure": link,
        }
    }
    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta['response']['init_point']
    id_pagamento = resposta['response']['id']
    return link_pagamento, id_pagamento









