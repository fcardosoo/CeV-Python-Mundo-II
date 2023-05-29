'''Ler vários numeros inteiros, parar quando digitar 999
Mostrar quantos nrs digitados e a soma, desconsiderando a flag'''

n = 0
soma = 0
c = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    soma += n
    c += 1
print('~'*40)
print(f'Foram digitados {c} valores que somaram {soma}!')
print('~'*40)
