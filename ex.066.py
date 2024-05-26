#066 Leia vários números inteiros, o programa parará quando digitar 999. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando  flag.
print('Para parar o programa digite 999')
s = 0
c = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    c +=1
    s+=n
print(f'A soma dos {c} valores foi {s}')