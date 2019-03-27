"""Crie um programa que leia o nome de uma cidade e diga se ela começa com Santo."""


cid = str(input('Digite o nome de uma cidade: ')).strip()

if cid[:5].upper() == 'SANTO':
    print('A cidade {} tem Santo em seu nome.'.format(cid))
elif cid[:3].upper() == 'SÃO':
    print('A cidade {} tem São em seu nome.'.format(cid))
else:
    print('A cidade {} não tem Santo ou São em seu nome.'.format(cid))
