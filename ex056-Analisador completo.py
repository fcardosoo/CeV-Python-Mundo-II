# ler o nome, idade e sexo de 4 pessoas
# Mostrar: A média de idade do grupo
# Qual o nome o homem mais velho
# Quantas mulheres tem menos de 20 anos

nomeh = str('')
idadeh = 0
mediai = 0
mulher20 = 0
for p in range(1, 5):
    print('----- {}ª -----'.format(p))
    n = str(input('Nome: '.strip()))
    s = str(input('Sexo (F/M): '.upper().strip()))
    i = int(input('Idade: '.strip()))

    mediai += i

    if p == 1 and s in 'Mm':
        nomeh = n
        idadeh = i
    if s in 'Mm' and i > idadeh:
        idadeh = i
        nomeh = n
    if s in 'Ff' and i < 20:
        mulher20 += 1

print('O homem mais velho é {}, com {} anos.'.format(nomeh, idadeh))
print('A média de idades do grupo é {} anos.'.format(mediai/4))
print('Ao todo são {} mulheres com menos de 21 anos.'.format(mulher20))