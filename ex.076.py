#076 Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ('Suporte para notebook', 35), ('Teclado', 74.90), ('Mouse', 61.95),('Mousepad', 35), ('Headphone', 169.70), ('Descanso de mesa', 30), ('Microfone', 90.99)
print('-'*40)
print('LISTAGEM DE PREÇOS'.center(35))
print('-'*40)
tamanho = 1
for produto, valor in listagem:
    valor = float(valor)
    print(f'{produto:.<29}R${valor:>8.2f}')