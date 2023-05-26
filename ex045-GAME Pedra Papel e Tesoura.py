# criar um jogo de jokempô com o pc
import time
import random
print('x x x '*5)
print('* * * * * * JOKEMPÔ * * * * * *')
print('x x x '*5)

jog = int(input('Escolha a sua opção:\n'
                    '1 - PEDRA\n'
                    '2 - PAPEL\n'
                    '3 - TESOURA\n'
                    'opção: '))
print('computador escolhendo....')

time.sleep(2)

comp = random.randint(1,3)
print(comp)
v = str('VENCEU')
p = str('PERDEU')

if jog == 1 and comp == 3:
    print('Você escolheu \033[1;31mPEDRA\033[m e o computador escolheu \033[1;31mTESOURA\033[m, você \033[1;31m{}\033[m!'.format(v))
elif jog == 1 and comp == 2:
    print('Você escolheu \033[1;31mPEDRA\033[m e o computador escolheu \033[1;31mPAPEL\033[m, você \033[1;31m{}\033[m!'.format(p))
elif jog == 2 and comp == 1:
    print('Você escolheu \033[1;31mPAPEL\033[m e o computador escolheu \033[1;31mPEDRA\033[m, você \033[1;31m{}\033[m!'.format(v))
elif jog == 2 and comp == 3:
    print('Você escolheu \033[1;31mPAPEL\033[m e o computador escolheu \033[1;31mTESOURA\033[m, você \033[1;31m{}\033[m!'.format(p))
elif jog ==3 and comp == 2:
    print('Você escolheu \033[1;31mTESOURA\033[m e o computador escolheu \033[1;31mPAPEL\033[m, você \033[1;31m{}\033[m!'.format(v))
elif jog == 3 and comp == 1:
    print('Você escolheu \033[1;31mTESOURA\033[m e o computador escolheu \033[1;31mPEDRA\033[m, você \033[1;31m{}\033[m!'.format(p))
elif jog == comp:
    print('EMPATE!!!')

""" 
if jog == 1 and comp == 3:
    print('Você escolheu {} e o computador escolheu {}, você \033[1;31m{}\033[m!'.format(jog, comp, v))
elif jog == 1 and comp == 2:
    print('Você escolheu {} e o computador escolheu {}, você \033[1;31m{}\033[m!'.format(jog, comp, p))
"""
