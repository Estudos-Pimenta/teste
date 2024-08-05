from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('', homepage, name="homepage"),
    path('loja/', loja, name="loja"),
    path('loja/<str:filtro>/', loja, name="loja"),
    path('produto/<int:id_produto>/', ver_produto, name="ver_produto"),
    path('produto/<int:id_produto>/<int:id_cor>/', ver_produto, name="ver_produto"),
    path('carrinho/', carrinho, name="carrinho"),
    path('checkout/', checkout, name="checkout"),
    path('adicionarcarrinho/<int:id_produto>/', adicionar_carrinho, name="adicionar_carrinho"),
    path('removercarrinho/<int:id_produto>/', remover_carrinho, name="remover_carrinho"),
    path('adicionarendereco/', adicionar_endereco, name="adicionar_endereco"),
    path('finalizarpedido/<int:id_pedido>/', finalizar_pedido, name="finalizar_pedido"),
    path('finalizarpagamento/', finalizar_pagamento, name="finalizar_pagamento"),
    path('pedidoaprovado/<int:id_pedido>/', pedido_aprovado, name="pedido_aprovado"),
    
    path('minhaconta/', minha_conta, name="minha_conta"),
    path('meuspedidos/', meus_pedidos, name="meus_pedidos"),
    path('fazerlogin/', fazer_login, name="fazer_login"),
    path('criarconta/', criar_conta, name="criar_conta"),
    path('fazerlogout/', fazer_logout, name="fazer_logout"),

    path('gerenciarloja/', gerenciar_loja, name="gerenciar_loja"),
    path('exportarrelatorio/<str:relatorio>/', exportar_relatorio, name="exportar_relatorio"),

    path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]


