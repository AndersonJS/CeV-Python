"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
"""


nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()

print('Prazer em conheçer!')
print('Seu primeiro nome é {}.'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))
