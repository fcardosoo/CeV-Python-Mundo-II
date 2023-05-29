''' Crie um simulador de caixa eletrônico
1º Pergunte o valor do saque (valor int)
2º O programa informa quantas células serão entregues.
considerar que o caixa possui cedulas de:
50; 20; 10 e 1 '''

print('==='*10)
print('{:^30}'.format('BANCO FÁCIL'))
print('~-~'*10)

valor = int(input('Qual o valor desejado? '))
total = valor
cedula = 50
contcedula = 0

while True:
    if total >= cedula:
        total -= cedula
        contcedula += 1
    else:
        if contcedula > 0:
            print(f'Total de cédulas {contcedula} de cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contcedula = 0
        if total == 0:
            break
print('~-~'*10)
print('Volte sempre ao BANCO FÁCIL!!!')