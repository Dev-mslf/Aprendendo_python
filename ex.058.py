#058 O computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from time import sleep
from random import randint
print('Olá, jogador! Será que você consegue adivinhar em que número estou pensando?')
sleep(3)
print('DICA: ELE ESTÁ ENTRE 0 E 10!')
sleep(3)
print('Vamos começar')
a = randint(0, 10)
r = int(input('Digite um número:'))
while r != a:
    print(f'Você errou. O número pensado foi o {a}. Vamos de novo!')
    a = randint(0, 10)
    r = int(input('Digite um número:'))
print(f'Você acertou! O número foi {a}')