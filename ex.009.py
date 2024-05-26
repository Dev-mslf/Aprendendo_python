#009 - programa que leia um número inteiro e mostre na tela a sua tabuada
numero = int(input('Escolha um número:'))
print('A seguir está a tabuada do ', numero)
print(
    ' {} x 1 = {}\n'.format(numero, 1*numero),
    '{} x 2 = {}\n'.format(numero, 2*numero),
    '{} x 3 = {}\n'.format(numero, 3*numero),
    '{} x 4 = {}\n'.format(numero, 4*numero),
    '{} x 5 = {}\n'.format(numero, 5*numero),
    '{} x 6 = {}\n'.format(numero, 6*numero),
    '{} x 7 = {}\n'.format(numero, 7*numero),
    '{} x 8 = {}\n'.format(numero, 8*numero),
    '{} x 9 = {}\n'.format(numero, 9*numero),
    '{} x 10 = {}\n'.format(numero, 10*numero)
)