"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de Desconto."""

v_produto = float(input('Qual o valor do Produto? '))
desc = (5*v_produto)/100

print('O Valor do Produto que era de R${} e agora com o desconto de 5% é de R${}'.format(v_produto, v_produto - desc))
