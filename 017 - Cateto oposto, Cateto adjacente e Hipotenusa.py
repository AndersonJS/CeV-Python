"""Faça um programa que leia um comprimento de cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa."""

'''co = float(input('Comprimento do cateto oposto : '))
ca = float(input(('Comprimento do cateto adjacente: ')))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))'''

from math import hypot  # Agora o mesmo desafio feito com o import.

co = float(input('Comprimento do cateto oposto :'))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))
