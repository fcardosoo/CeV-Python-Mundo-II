# criar um jogo de jokempô com o pc
import time
import random

print('- - - '*5)
print('* * * * * * JOKEMPÔ * * * * * *')
print('- - - '*5)

j = int(input('Escolha sua opção:\n' # MENU de escolha do jogador
              '1 - Pedra\n'
              '2 - Papel\n'
              '3 - Tesoura\n'
              'Sua escolha é: '))

if j == 1: # substituindo valor por texto
    jog = str('PEDRA')
elif j == 2:
    jog = str('PAPEL')
else:
    jog = str('TESOURA')

print('Você escolheu {}'.format(jog))
print(' ')
time.sleep(.5)
print('JO')
time.sleep(.5)
print('KEN')
time.sleep(.5)
print('PO')
time.sleep(.5)


c = random.randint(1, 3) # computador escolhendo randomicamente

if c == 1: # substituindo valor por texto
    com = str('PEDRA')
elif c == 2:
    com = str('PAPEL')
else:
    com = str('TESOURA')
print('O computador escolheu {}.'.format(c))
print('O computador escolheu {}.'.format(com))

#Testando o ganhador:
if (j == 1 and c == 3) or (j == 2 and c == 1) or (j == 3 and c == 2):
    print('PARABÉNS, você escolheu \033[1;31m{}\033[m e o computador escolheu\n \033[1;31m{}\033[m, você \033[1;32mVENCEU\033[m!!!'.format(jog, com))
elif j == c:
    print('Você escolheu \033[1;31m{}\033[m e o computador escolheu\n \033[1;31m{}\033[m, deu \033[1;32mEMPATE\033[m!!!'.format(jog, com))
else:
    print('Você escolheu \033[1;31m{}\033[m e o computador escolheu\n \033[1;31m{}\033[m, você PERDEU!!!'.format(jog, com))