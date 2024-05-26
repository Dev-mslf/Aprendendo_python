#073 Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados
# b) Os últimos 4 colocados da tabela
# c) Uma lista com os times times em ordem alfabética
# d) Em que posição na tabela está o time da chapecoense
colocados = 'Chapecoense','Athletico','Bahia','Flamengo','Botafogo','São Paulo','Cruzeiro','Atlético','Bragantino','Palmeiras','Internacional','Fortaleza','Gêmio','Vasco','Criciúma', 'Juventude', 'Corinthians','Fluminense','Vitória','Atlético-GO'
print(f'Os cinco primeiros colcados são {colocados[:5]}')
print(f'Os últimos 4 colocados são {colocados[-4:]}')
print(f'Times em ordem alfabética {sorted(colocados)}')
if 'Chapecoense' in colocados:
    print(f'O Chapecoense está na {colocados.index('Chapecoense')+1}ª posição')