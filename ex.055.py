#055 Leia um número inteiro e diga se ele é ou não um número primo
quantidade_divisor= 0
numero = int(input('Digite um número: '))
for c in range(1, numero+1):
    if numero % c ==0:
        quantidade_divisor += 1
if quantidade_divisor > 2 or quantidade_divisor ==1:
    print('Esse número não é primo')
else:
    print('Esse número é primo!')