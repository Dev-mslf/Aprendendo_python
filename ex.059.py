#059 Leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
print('--------- MENU---------\n'
      ' [1] somar\n [2] multiplicar\n [3] maior\n [4] novos números\n [5] sair do programa')
opc = int(input('Informe o número da opção desejada: '))
while opc != 5:
    if opc==1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}.')
        print('Fim da operação.\n Escolha a próxima operação.')
        opc = int(input('Informe o número da opção desejada: '))
    if opc == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}')
        print('Fim da operação.\n Escolha a próxima operação.')
        opc = int(input('Informe o número da opção desejada: '))
    if opc == 3:
        if n1>n2:
            print(f'O maior número é o {n1}')
        if n2>n1:
            print(f'O maior número é o {n2}')
        print('Fim da operação.\n Escolha a próxima operação.')
        opc = int(input('Informe o número da opção desejada: '))
    if opc == 4:
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
        opc = int(input('Informe o número da opção desejada: '))
print('Você selecionou a opção 5 .. Saiu do programa.')