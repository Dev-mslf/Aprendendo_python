#022 Crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas
# com tds as letras minusculas
# quantas letras ao todo sem considerar espaços
# quantas letras tem o primeiro nome

nome = input('Digite seu nome completo:')
print('Esse é seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Esse é o seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Seu nome completo possui {} letras'.format(len(nome.replace(' ',''))))
delimitar = nome.find(' ')
print('O seu primeiro nome tem {} letras!'.format(len(nome[:delimitar])))
