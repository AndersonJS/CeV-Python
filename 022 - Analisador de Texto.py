"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas
- O nome com todas as letras minusculas
- Quantas letras tem ao todoo ( sem considerar os espaços )
- Quantas letras tem o primeiro nome."""


def n():
    print('-'*30)


n()
nome = input('Digite o seu nome completo: ').strip()
separa = nome.split()  # Estava colocando strip no lugar do split

print('Seu nome com todas as letras maiusculas:\n{}'.format(nome.upper()))

n()
print('Seu nome com todas as letras minusculas:\n{}'.format(nome.lower()))

n()
print('Seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
