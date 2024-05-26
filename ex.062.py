#062 melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
termo1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
print(termo1)
max = 9
c = 0
while c != max:
    termo1 += r
    c+=1
    print(termo1)
while max != 0:
    max = int(input('Quantos termos você ainda quer ver? '))
    c = 0
    while c != max:
        termo1 += r
        c += 1
        print(termo1)
print('Você saiu do programa')