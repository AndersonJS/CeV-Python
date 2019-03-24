"""Faça um programa que leia o ângulo e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))  # Não estava conseguindo pois tinha esquecido de converte o grau para radiano.
cose = cos(radians(ang))
tang = tan(radians(ang))

print('Ângulo {}º'.format(ang))
print('Seu Seno é {:.2f}'.format(sen))
print('Seu coseno é {:.2f}'.format(cose))
print(('Sua Tangente é {:.2f}'.format(tang)))
