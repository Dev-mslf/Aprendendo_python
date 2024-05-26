#016 Leia um número real e mostre a sua porção inteira
from math import trunc
num = float(input('Digite um número:'))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
