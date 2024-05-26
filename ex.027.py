#027 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = input('Digite nome completo:').strip()
print("Seu primeiro nome é {}".format(nome[:(nome.find(' '))]))
print('Seu último nome é{}'.format(nome[nome.rfind(' '):]))
# OU
#n = str(input('Digite seu nome completo:')).strip()
#nome = n.split()
#print('Seu primeiro nome é {}'.format(nome[0]))
#print('Seu último nome é {}'.format(nome[len(nome)-1]))