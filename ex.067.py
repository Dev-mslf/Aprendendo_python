#067 mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número for negativo.
n = int(input('Quer ver a tabuada de qual valor? '))
c = 1
while True:
    if n>0 and c<=11:
        print(f'{n} x {c} = {n*c}')
        c+=1
    if n>0 and c == 11:
        n = int(input('Quer ver a tabuada de qual valor? '))
        c = 1
        c+=1
    if n < 0:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')