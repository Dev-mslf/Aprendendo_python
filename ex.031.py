#031 Pergunte a distancia de uma viagem em km. calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
d = float(input('Quantos KM tem o trajeto?'))
if d <= 200:
    print(f'A passagem custa R${(0.5*d):.2f}')
else:
    print(f'A passagem custa R${(0.45*d):.2f}')