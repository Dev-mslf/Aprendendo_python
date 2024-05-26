#071 Simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues
# obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
print('BANCO DA GABI')
print('='*24)
valor = int(input('Que valor você quer sacar?\n'
          'Apenas valores inteiros!\n'
          'R$'))
cedulas_50 = (valor//50)
cedulas_20 = (valor % 50)//20
cedulas_10 = ((valor % 50)%20)//10
cedulas_1 = (((valor % 50)%20)%10)//1
while True:
    if cedulas_50 > 0:
        print(f'Cédulas de R$50: {cedulas_50}')
    if cedulas_20 > 0:
        print(f'Cédulas de R$20: {cedulas_20}')
    if cedulas_10 > 0:
        print(f'Cédulas de R$10: {cedulas_10}')
    if cedulas_1 > 0:
        print(f'Cédulas de R$1: {cedulas_1}')
    break