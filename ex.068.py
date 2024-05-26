#068 Um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder.
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*14)
c = 0
while True:
    valor = int(input('Escolha um valor: '))
    par_impar = input('Você escolhe par ou ímpar? [P/I] ').strip().upper()[0]
    print('-'*28)
    from random import randint
    comp = randint(0,10)
    total = valor+comp
    soma = ''
    if total % 2 == 0:
        soma = 'PAR'
    else:
        soma = 'IMPAR'
    print(f'Você jogou {valor} e o computador jogou {comp}. O total é {total}, resultando em um número {soma}.')
    print('-'*28)
    if soma[0] == par_impar:
        print('Você venceu!\n'
        'Vamos novamente...')
        print('=-' * 14)
        c+=1
    else:
        print('Você perdeu!')
        print('=-'*14)
        break
print(f'GAME OVER! Você venceu {c} vezes.')