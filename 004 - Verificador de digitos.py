"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis
sobre ela."""

digito = input('Digite algo: ')


print()
print('O Tipo Primitivo é ', type(digito))
print('É alfanumérico ( letra e número ): ', digito.isalnum())
print('É alfabético ( Letra ): ', digito.isalpha())
print('É um número decimal): ', digito.isdecimal())
print('É apenas dígitos): ', digito.isdigit())
print('É válido: )', digito.isidentifier())
print('É minusculo: ', digito.islower())
print('É número: ', digito.isnumeric())
print('É imprimivél: ', digito.isprintable())
print('É espaço em branco: ', digito.isspace())
print('A Primeira letra é Maiuscula: ', digito.istitle())
print('São letras maiusculas: ', digito.isupper())
