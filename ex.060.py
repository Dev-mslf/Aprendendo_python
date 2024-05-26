#060 Faça um programa que leia um número qualquer e mostre o seu fatorial
n = int(input('Digite o número para calcularmos o seu fatorial: '))
fat= n*(n-1)
c = 1
while c != (n-1):
    c += 1
    fat = fat * (n-c)
print(f'{n}! = {fat}')