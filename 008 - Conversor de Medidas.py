"""Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros."""

m = float(input('Digite um valor em metros: '))
cm = m*100
ml = m*1000

print('{} Metros equivale a {} Centimetros e a {} Milimetros.'.format(m, cm, ml))
