"""Crie um programa que leia um nome de uma pessoa e diga se ela tem 'Silva' no nome."""


nome = str(input('Digite seu nome Completo: ').strip())
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
