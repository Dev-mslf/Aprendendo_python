#034 digite salário e calcule o valor do aumento. Para salários superiores a 1250 calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15%

s = float(input('Digite o valor do seu salário:'))
if s > 1250:
    print(f'O seu salário receberá um aumento de 10%. Portanto, o seu novo salário é R${s*1.1:.2f}')
elif s<= 1250:
    print(f'O seu salário receberá um aumento de 15%. Portanto, o seu novo salário é R${s * 1.15:.2f}')