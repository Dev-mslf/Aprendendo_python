#045 PEDRA PAPEL OU TESOURA
from random import choice
lista = ['PEDRA', 'PAPEL', 'TESOURA']
comp = choice(lista)
print('Vamos jogar Jokenpô!\n'
      'Pronto?')
print('3...\n'
      '2...\n'
      '1...\n')
jogador = input('Pedra, Papel ou tesoura?').upper().strip()
if comp == jogador:
    print(f'Computador: {comp}')
    print('Empate!')
elif comp == 'PEDRA' and jogador == 'PAPEL':
    print(f'Computador: {comp}')
    print('Você venceu!')
elif comp == 'PEDRA' and jogador == 'TESOURA':
    print(f'Computador: {comp}')
    print('Você perdeu!')
elif comp == 'PAPEL' and jogador == 'PEDRA':
    print(f'Computador: {comp}')
    print('Você perdeu!')
elif comp == 'PAPEL' and jogador == 'TESOURA':
    print(f'Computador: {comp}')
    print('Você venceu!')
elif comp == 'TESOURA' and jogador == 'PEDRA':
    print(f'Computador: {comp}')
    print('Você venceu!')
elif comp == 'TESOURA' and jogador == 'PAPEL':
    print(f'Computador: {comp}')
    print('Você perdeu!')
else:
    print('hmm... Algo deu errado. Verifique se você escreveu corretamnte e tente novamente!')