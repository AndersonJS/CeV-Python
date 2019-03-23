"""Faça um programa que leia um número inteiro  e mostre na tela o seu Antecessor e Sucessor."""

n = int(input('Digite um número: '))
ant = n - 1
suc = n + 1

print(' ')
print('O Antecessor de {} é {} e o seu sucessor é o {}.'.format(n, ant, suc))
print('=' * 45)
print('Antecessor de {} é {} e o sucessor é {}.'.format(n, n-1, n+1))  # Assim a variavél ant e suc podem ser tiradas.
