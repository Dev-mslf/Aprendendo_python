#063 Leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.
n = int(input('Digite um número: '))
seq = 0
termo0 = 0
termo1 = 1
n-=2
print('0 -> 1', end=' ')
while seq != n:
    termo0 += termo1
    termo1 += termo0
    if seq < n:
        print(f'-> {termo0}', end = ' ')
    seq+=1
    if seq < n:
        print(f'-> {termo1}', end= ' ')
    seq += 1