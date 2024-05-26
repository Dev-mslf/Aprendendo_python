#049 Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que utilizando um laço for
n = int(input('Escolha um número:'))
print(f'A seguir está a tabuada do {n}')
for c in range(1,11):
    print(f'{n} x {c} = {n*c}')