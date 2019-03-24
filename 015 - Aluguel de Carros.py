"""Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos
quais foi alugado e calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado."""

dia = int(input('Digite a quantidade de dias alugado: '))
km = float(input('Digite a quantidade de Km rodados pelo veículo: '))
v_dia = dia * 60
v_km = km * 0.15

print('='*35)
print('Calculador de aluguel para Veículo.')
print('='*35)
print(' ')
print('Valor do Dias Alugados é de R${} \nValor do Km Rodados que é R${} \nValor Total a pagar: R${}'.format(v_dia, v_km, v_dia+v_km))  # No menu, em view na opção active editor ative use soft Wraps
