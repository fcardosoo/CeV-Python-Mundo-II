# Ler data de nasc. e determinar a categoria do
# atleta de natação
# Até 9 - Mirim
# Até 14 - Infantil
# Até 19 - Junior
# Até 25 - Sênior
# Acima - Master

from datetime import date

print('=!=!='*9)
print('CLASSIFICAÇÃO DE CATEGORIAS DE COMPETIÇÃO!')
print('*-*-'*11)

ano = date.today().year
a = int(input('Informe seu ano de nascimento (aaaa): '))
idade = ano - a

m = str('Mirim')
i = str('Infantil')
j = str('Júnior')
s = str('Sênior')
ms = str('Master')

print('-*-'*20)

if idade <= 9:
    print('Você possui {} anos, logo pertence a categoria\033[1;31m {}\033[m!'.format(idade, m))
elif idade <= 14:
    print('Você possui {} anos, logo pertence a categoria\033[1;31m {}\033[m!'.format(idade, i))
elif idade <= 19:
    print('Você possui {} anos, logo pertence a categoria\033[1;31m {}\033[m!'.format(idade, j))
elif idade <= 25:
    print('Você possui {} anos, logo pertence a categoria\033[1;31m {}\033[m!'.format(idade, s))
else:
    print('Você possui {} anos, logo pertence a categoria\033[1;31m {}\033[m!'.format(idade, ms))
print('-=-'*20)