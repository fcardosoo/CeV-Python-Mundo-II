#Ler 7 datas de nascimento e informar
#quantos são maiores/menores de 21 anos

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pes in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pes)))
    idade = date.today().year - nasc
    #print('Esta pessoa tem {} anos de idade'.format(idade))
    if idade >= 21:
        #print('Essa pessoa é maior!')
        totmaior += 1
    else:
        #print('Essa pessoa é menor!')
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade.'.format(totmenor))
