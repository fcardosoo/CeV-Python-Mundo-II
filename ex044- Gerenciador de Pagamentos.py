# calcular preço a pagar considerando:
# preço normal e condição de pagamento
# A vista ou chq - 10% de desc.
# A vista cartão - 5% de desc.
# em 2x no cartão: preço normal
# 3 vezes ou mais no cartão: 20% de acresc.

print(' ')
print('{:=^40}'.format(' CREDIÁRIO '))
print(' ')

v = float(input('Qual o valor das compras? '))
c = int(input('Escolha a condição de pagamento:\n'
              '1 - A vista dinheiro/cheque\n'
              '2 - A vista cartão débito/crédito\n'
              '3 - 2 vezes no cartão\n'
              '4 - 3 ou mais vezes no cartão\n'
              'Informe sua preferência: '))

if c == 1:
    print('Você receberá 10% de desconto!!!')
    print('O valor de uas compras ficará R${}'.format(v*0.9))
elif c == 2:
    print('Você receberá 5% de desconto!!!')
    print('O valor de uas compras ficará R${}'.format(v * 0.95))
elif c == 3:
    print('Para esta opção de compra não há descontos cadastrados!!!')
    print('Suas compras ficarão 2 vezes de R${}'.format(v/2))
elif c == 4:
    p = int(input('Quantas parcela?'))
    print('Para esta opção de compra terá um acréscimo de 20%!!!')
    print('Suas compras ficarão em {} vezes de R${}'.format(p, (v*1.2)/p))
else:
    print('Opção não cadastrada!')

print('*-*-'*15)