frase = 'curso em Video Python'
nome = 'Anderson Jalasko dos Santos'
nome1 = 'Jesina Silva Aguiar'

print(frase[:13:2])
print(nome[::-1])
print(nome1[::-1])

"""Recursos Para Análisar um texto."""
print(len(frase))
print(len(nome))  # O len contra quantas letras + o espaço tem no texto.
print(len(nome1))

print(frase.count('o'))
print(nome.count('a'))  # count conta quantas vezes aparece a letra
print(nome.count('a', 0, 13))  # count com o fatiamento, achei estranho pois neste momento acostumei com : para fatia.

print(frase.find('deo'))  # mostra onde começa o deo dentro da memoria, lembra que a contagem começa no 0.
print(nome.find('a'))  # o find diferencia maiusculo de minusculo.

print('curso' in frase)  # tambem pode usa o operador in para avaliar se uma palavras esta no texto.

"""Resursos de Transformação."""
print(frase.replace('Python', 'Android'))  # com replace pode trocar uma palavras por outra.
print(frase.upper())  # passando todas as letras da frase para maiusculo com método upper.
print(frase.lower())  # passando todas as letras da frase para minusculo
print(frase.capitalize())  # primeira letra maiuscula e as demais nimusculas.
print(frase.title())  # a primeira de cada letra maiscula e as demais minusculas.

var = '   Aprenda Python   '
print(var.strip())  # strip tira os espaço inuteis de uma frase, do começo e final da frase.
print(var.rstrip())  # tira apenas os espaço do lado direito da frase
print(var.lstrip())  # tira apenas os espaço do lado esquerdo.

"""Divisão"""
lista = (frase.split())  # coloque em uma variavél pra testa, split forma uma lista dividido cada palavra
print(lista)

print(frase.strip())

"""Junção"""
print(frase)
print('-'.join(frase))  # c-u-r-s-o- -e-m- -V-i-d-e-o- -P-y-t-h-o-n
