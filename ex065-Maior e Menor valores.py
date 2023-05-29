'''Ler varios numeros
mostrar a média; o maior e o menor
perguntar se o usuario deseja continuar'''

print('~'*20)
print('***** Números *****')
print('~'*20)

num = 0
maior = 0
menor = 0
soma = 0
contador = 0
conti = 'S'

while conti in 'Ss':
    num = int(input('Digite um número: '))
    contador += 1
    soma += num
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    conti = str(input('Deseja continuar? '.upper()))
media = soma/contador
print('Você digitou {} números e a média foi {:.2f}.'.format(contador, media))
print(f'O maior valor foi {maior} e o menor foi {menor}')
