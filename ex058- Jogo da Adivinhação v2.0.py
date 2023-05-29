''' Jogo!!!
sortear um número entre 0 e 10
o jogador tenta até advinhar, quando acertar
o pc dá parabens e informa o numero de palpites'''

from random import randint

sorteio = randint(1, 10)
palpite = int(input('Tente adivinhar o número que\n eu pensei entre 1 e 10: '))
cont = 1

while palpite != sorteio:
    print('ERROU!!!')
    if palpite > sorteio:
        print('Menos!')
    else:
        print('Mais!')
    cont += 1
    palpite = int(input('Tente novamente: '))
print('Parabéns!!! Eu pensei no número \033[1;33m{}\033[m, e você precisou de \033[1;31m{}\033[m palpites para advinhar!!!'.format(sorteio, cont))
