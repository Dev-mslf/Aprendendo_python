#036 Escreva um programa para aprovar o emprèstimo bancário para a coompra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# calcule o valor da prestação mensal,sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Quanto custa a casa?'))
salario = float(input('Salário do comprador:'))
anos = int(input('Em quantos anos pretende pagar?'))
valordaPrestacao = casa/(12*anos)
if valordaPrestacao > 0.3*salario:
    print('Empréstimo negado \n'
          'Você deverá tentar novamente, extendendo o prazo de pagamento.')
elif valordaPrestacao <= 0.3*salario:
    print(f'Empréstimo aprovado! A parcela será de R${valordaPrestacao:.2f}, com o total de {anos*12} parcelas, para que seja quitado o valor do imóvel.')