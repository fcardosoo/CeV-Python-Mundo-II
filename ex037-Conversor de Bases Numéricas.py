#Peça um número e dê opção de converter
# o número para binário, octadecimal e hexadecimal
# dê a resposta.

print('- -'*15)
print('************* CONVERSOR DE BASE *************')
print('= ='*15)

n = int(input('Informe o número que deseja converter: '))
c = int(input('Escolha:\n(1) para Binário; \n(2) para Octadecimal; \n(3) para Hexadecimal.\nInforme: '))

if c == 1:
# Na resp vou fatiar a partir do terceiro número com o [2:] para mostrar apenas números
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif c == 2:
    print('{} convertido para OCTADECMAL é igual a {}'.format(n, oct(n)[2:]))
elif c == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, escolha 1, 2 ou 3!')