#070 Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000
# qual é o nome do produto mais barato
print('-'*24)
print('SUPER BARATÃO')
print('-'*24)
cont = 'S'
total = 0
mais_de_mil = 0
mais_barato = 0
nome_mais_barato = ''
rodada = 1
while True:
    if cont == 'S':
        nome = input('Nome do produto: ')
        preco = float(input(f'Valor: R$'))
        total += preco
        if preco > 1000:
            mais_de_mil+=1
        if rodada == 1:
            mais_barato = preco
            nome_mais_barato = nome
            rodada+=1
        elif rodada > 1:
            if preco<mais_barato:
                mais_barato = preco
                nome_mais_barato = nome
        cont = input('Quer adicionar mais itens? [S/N] ').strip().upper()[0]
    elif cont not in 'SN':
        cont = input('Quer adicionar mais itens? [S/N] ').strip().upper()[0]
    elif cont == 'N':
        break
print('-'*24)
print('TOTAL DA COMPRA')
print(f'O total da compra foi R${total:.2f}\n'
      f'Temos {mais_de_mil} produtos custando mais de R$1000\n'
      f'O produto mais barato foi "{nome_mais_barato}" que custa R${mais_barato}')