#075 Desenvolva um programa que leia quatro valores pelo teclaco e guarde-os em uma tupla. No final, mostre:
# a) quantas vezes apareceu o valor 9
# b) em que posição foi digitado o primeiro valor 3
# c) quais foram os números pares
num_1= input('Digite um número: ')
num_2= input('Digite outro número: ')
num_3= input('Digite mais um número: ')
num_4= input('Digite o último número: ')
tupla = num_1, num_2, num_3, num_4
print(f'Você digitou os valores {tupla}')
c=0
for num in tupla:
    if num == '9':
        c+=1
print(f'O valor 9 apareceu {c} vezes')
if '3' in tupla:
    print(f'O valor 3 apareceu na {tupla.index('3')+1}ª posição')
else:
    print('O valor 3 não apareceu nenhuma vez')
print('Os valores pares digitados foram', end = ' ')
pares = ''
for num in tupla:
    num = int(num)
    if num % 2 == 0:
        pares = num
        print(f'{pares}', end =' ' )