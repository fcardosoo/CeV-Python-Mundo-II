'''Ler numeros, quando '999' parar
mostrar quantos numeros foram digitados
e a soma entre eles, desconsiderando o 999'''

print('~'*40)
print('Contagem')
print('~'*40)

n = 0
contador = 0
soma = 0

while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        contador += 1
        soma += n
print('Você inseriu {} números, que somaram {}'.format(contador, soma))