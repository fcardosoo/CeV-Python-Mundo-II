#peça 2 números inteiros e compare-os; mostre qual é o maior ou se são iguais

print('*'*45)
print('\033[1;35;47m COMPARADOR DE NÚMEROS!!!\033[m')
print('*'*45)

n1 = int(input('Digite o primeiro número a ser comparado: '))
n2 = int(input('Didite o segundo número a ser comparado: '))

print('*'*45)
if n1>n2:
    print('O número {} é maior do que o número {}.'.format(n1, n2))
    print('{} > {}'.format(n1, n2))
elif n2>n1:
    print('O número {} é maior do que o número {}.'.format(n2, n1))
    print('{} < {}'.format(n1, n2))
else:
    print('Os números {} e {} são iguais.'.format(n1, n2))
    print('{} = {}'.format(n1, n2))
print('-x-'*15)