'''Solicitar um número e mostrar
o seu fatorial'''

print('=-='*10)
print('*'*10,'FATORIAL','*'*10)
print('=-='*10)

n = int(input('Digite um número qualquer ou ZERO para SAIR!' ))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c>1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))