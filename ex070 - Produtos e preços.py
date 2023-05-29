''' ler nome e preço de produtos perguntar a cada cadastro se continua Mostrar: a) Total dos produtos
b) Quantos produtos custam mais de $1000 Qual é o nome do produto mais barato '''

print('~'*30)
print('**** COMPRAS ****')
print('~'*30)

produto = str('')
preco = float(0)
total = mil = contador = baratopr = int(0)
barato = str('')
continuar = str(' ')

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto R$ '))
    contador += 1
    total += preco
    if contador == 1 or preco < baratopr:
        barato = produto
        baratopr = preco
    if preco >1000:
        mil += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Você comprou {contador} itens, \n'
      f'totalizando R${total} \n '
      f'{mil} produtos custaram mais de Mil Reais.\n'
      f'O produto mais barato é {barato}!')
print('Obrigado pela preferência. Volte sempre!!!')
print('~'*30)
