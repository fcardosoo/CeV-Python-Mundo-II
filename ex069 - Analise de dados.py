'''Ler idade e sexo. A cada registro perguntar
se quer prosseguir.
Mostrar: qnts + 18 anos; qnts homens;
qnts mulheres <20'''

maiores = homens = mulhM = 0

while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o Sexo [M/F]: ').upper().strip()[0])
    idade = int(input('Digite a idade: '))
    if idade>= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <20:
        mulhM += 1
    prosseguir = ' '
    while prosseguir not in 'SN':
        prosseguir = str(input('Deseja prosseguir? ').upper().strip())
    if prosseguir == 'N':
        break
print(f'Os registros apresentam:\n'
      f'{maiores} maiores de 18 anos;\n'
      f'{homens} homens;\n'
      f'{mulhM} Mulheres com menos de 20 anos.')
print('~'*30)
print('FIM!')