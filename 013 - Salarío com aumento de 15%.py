"""Faça um algoritmo que leia um Salarío de um funcionário e mostre seu novo salarío, com 15% de Aumento."""

sal = float(input('Digite o seu salarío: '))
aumento = sal+(15*sal)/100

print('Seu salarío de R${} + 15% de aumento é de R${}'.format(sal, aumento))
