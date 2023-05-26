# calcular a soma entre todos os nrs ímpares
# multiplos de 3 entre 1 e 500

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 ==0:
        print(c)
        s += c
        cont += 1
print('A soma dos {} valores ímpares entre 1 e 500, \nmultiplos de 3 é {}.'.format(cont, s))
