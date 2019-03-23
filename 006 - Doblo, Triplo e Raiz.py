"""Faça um algoritmo que leia um número e mostre seu doblo, triplo e sua raiz."""

num = int(input('Digite um número: '))
dob = num**2
trip = num**3
raiz = num**(1/2)

print('O número {} tem como doblo o {} e o triplo é {} e sua Raiz Quadrada vale {}.'.format(num, dob, trip, raiz))
