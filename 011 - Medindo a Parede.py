"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pinta-lá, sabendo que 1l = 2m²"""

larg = float(input('Qual é a Largura da Parede em metros: '))
alt = float(input('Agora me diga a altura também em metros: '))
area = larg*alt

print('A Parede mede {}m² e com {}Litros de tinta você pode tinta-lá.'.format(area, area/2))
