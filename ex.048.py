#048 Calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
print('Números ímpares, múltiplos de 3, entre 1 e 500:')
s=0
for c in range(1,500,+2): #aqui ele já pega só os números ímpares
    if c %3==0: #Aqui delimita aqueles que são multiplos de 3
        print(c)
        s += c
print(f'A soma dos números ímpares, múltiplos de 3, que existem entre 1 e 500, é {s}')