#026 Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input('Digite uma frase:')
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A letra A aparece na primeira vez na posição ', frase.find('a'))