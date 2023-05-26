#criar uma tabuada usando repetições (ex009)

n = int(input('Digite o nr que deseja a tabuada: '))

print('*'*5, 'TABUADA DO', n, '*'*5)
for c in range(1, 11):
    print('{:2} x {:2} = {:2}'.format(c, n, c*n))
print('Fim')