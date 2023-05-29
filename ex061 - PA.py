'''Refazer o ex051, ler o primeiro
termo da uma PA e a razão. Mostrar os
10 primeiros termos da PA'''

print('-=-'*10)
print('PROGRESSÃO ARITMÉTICA')
print('-=-'*10)

primTermo = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
termo = primTermo
contador = 1

while contador <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razao
    contador += 1
print('FIM')

