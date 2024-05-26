#019 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
n1= input('1- Nome do aluno:')
n2= input('2- Nome do aluno:')
n3= input('3- Nome do aluno:')
n4= input('4- Nome do aluno:')
list = [n1,n2,n4,n4]
print('O escolhido foi {}'.format(random.choice(list)))