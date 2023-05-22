# Ler o ano de nascimento e determinar se:
# Ainda falta (anos) para ele se alistar
# Se já está no prazo
#Ou se já passou o prazo

print('-x-'*15)
print('*********** ALISTAMENTO ***********')
print('-=-'*10)

n = int(input('Informe o ano de nascimento (aaaa): '))

if (2021 - n) == 18:
    print('Você deve se alistar neste ano!!!')
elif (2021 - n) < 18:
    print('Você tem {} anos, ainda faltam {} anos para você se alistar.'.format(2021-n, 18-(2021-n)))
else:
    print('Atualmente você tem {} anos, já se passaram {} anos de você ter se alistado.'.format(2021-n, (2021-n)-18))
print('-=-'*10)