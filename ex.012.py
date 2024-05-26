#012 - faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Qual é o preço do produto?'))
print('Você recebeu um desconto de 5% em cima do valor do produto! De R${:.2f}, por R${:.2f}!'.format(preco, preco-0.05*preco))