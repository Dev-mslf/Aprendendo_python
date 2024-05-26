#054 Leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
import datetime
year = datetime.datetime.now().year
pessoa_maior = 0
pessoa_menor = 0
for c in range(1,8):
    a = int(input('Digite o ano de nascimento: '))
    if year - a >= 21:
        pessoa_maior += 1
    else:
        pessoa_menor += 1
print(f'Dentro dos anos informados, temos {pessoa_maior} pessoas maiores de idade\ne {pessoa_menor} pessoas menores de idade.')