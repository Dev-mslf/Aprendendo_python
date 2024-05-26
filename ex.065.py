#065 Leia vários números ent, no final, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n = 0
c = 0
s = 0
maior = 0
menor = 0
cont = 'SIM'
while cont == 'SIM':
    n = int(input('Digite um número: '))
    s+= n
    c+=1
    cont = input('Quer continuar? [sim/não] ').upper().strip()
    if c ==1:
        menor = n
        maior = n
    if c >1:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'A média entre os números foi {s/c:.2f}\n'
      f'O maior número foi {maior}\n'
      f'O menor número foi {menor}')