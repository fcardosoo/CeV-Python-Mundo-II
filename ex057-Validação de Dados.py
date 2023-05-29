''' Ler sexo da pessoa,
só aceitar M ou F, solicitar o valor
correto novamente'''

s = str('')
while s != 'S':
    s = str(input('Qual o seu sexo M/F? ').upper().strip()[0])
    if s in 'MF':
        print('Valor registrado com sucesso!\nInforme outro valor.')
    else:
        print('Informação incorreta, informe M ou F.')
print('Fim')