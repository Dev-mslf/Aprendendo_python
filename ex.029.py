#029 Leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7 reais por cada km acima do limite.
v = float(input('Velocidade atual do carro:'))
if v > 80:
    print('Você ultrapassou o limite de velocidade! Foi multado.')
    print(f'O valor da multa é de R${((v-80)*7):.2f}')
else:
    print('Ótimo! Você está dirigindo dentro do parâmetro de velocidade permitido.')