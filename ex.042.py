#042 Se o conjunto de retas puder formar um triângulo, informar qual
r1 = float(input('comprimento da primeira reta:'))
r2 = float(input('comprimento da segunda reta:'))
r3 = float(input('comprimento da terceira reta:'))

if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    print('Podem formar um triângulo')

    if r1 == r2 == r3:
        print('Esse conjunto de retas formam um triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse conjunto de retas formam um triângulo isósceles')
    elif r1 != r2 != r3:
        print('Esse conjunto de retas formam um triângulo escaleno')
else:
    print('Não podem formar um triângulo')