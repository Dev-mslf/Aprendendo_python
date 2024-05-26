#008 - leia um valor em metros e o exiba convertido em centímetros e milímetros
valor = float(input('Quantos metros você deseja converter?'))
paraCentimetros = (valor*100)
paraMilimetros = (valor*1000)
print('O valor em centímetros é {:.0f} e o valor em milímetros é {:.0f}'.format(paraCentimetros, paraMilimetros))