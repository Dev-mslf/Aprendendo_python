#057 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = input('Digite o seu sexo [M/F]: ').upper().strip()
while s not in 'MF':
    print('Opa! algo deu errado. Verifique se você digitou M ou F para sinalizar o seu sexo e tente novamente.')
    s = input('Digite o seu sexo [M/F]: ').upper().strip()
if s == 'F':
    print('Seu sexo é feminino!')
if s == 'M':
    print('Seu sexo é masculino!')