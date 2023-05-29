'''Ler um n inteiro e mostrar
na tela os n primeiros elementos de uma
sequencia de Fibonacci'''

print('-'*40)
print('Sequência de FIBONACCI')
print('-'*40)
n = int(input('Quantos termos você deseja exibir? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
contador = 3

while contador <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    contador += 1
    t1 = t2
    t2 = t3
print('-> FIM')
print('~'*40)