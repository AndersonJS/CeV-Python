"""Crie um programa que leia um número real pelo teclado e mostre a sua porção inteira"""

'''import math

num = float(input('Digite um Número Real: '))

print('O valor digitado {} tem como parte inteiro o número {}'.format(num, math.trunc(num)))'''


'''from math import trunc

num = float(input('Digte um Número Real: '))

print('O valor digitado {} tem com parte inteira o número {}'.format(num, trunc(num)))'''


num = float(input('Digite um número real: '))

print('O valor digitado {} tem como parte inteira o número {}'.format(num, int(num)))
