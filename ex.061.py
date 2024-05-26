#061 Leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
c = 0
print(termo1)
while c != 9:
    termo1 += r
    c+=1
    print(termo1)