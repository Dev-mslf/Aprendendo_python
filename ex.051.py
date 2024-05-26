#051 Leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
primeiro = int(input('Digite o primeiro termo da PA:'))
razao = int(input('A razão da PA será de:'))
decimo = primeiro + (10-1) * razao
for c in range (primeiro, decimo + razao, razao):
    print(c)
