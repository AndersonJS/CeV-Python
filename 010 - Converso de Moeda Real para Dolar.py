"""Crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos dolares ela pode comprar."""

real = float(input('Quantos Reais você tem? '))

print(' ')
print('Com R${} da para comprar ${:.2f}Dolar.'.format(real, real/3.91))  # 3.91 Cotação do dolar de 23 de Março de 2019.
