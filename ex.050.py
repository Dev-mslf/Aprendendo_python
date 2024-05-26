#050 Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for ímpar, desconsidere-o.
soma=0
for c in range(1,7):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        soma = soma + n
print(soma)