#032 Faça um programa que leia um ano qualquer e mostre se ele é bissexto
a = int(input('Qual é o ano?'))
if  (a % 4 == 0) and (a % 100 !=0) or (a % 400 == 0) :
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto')