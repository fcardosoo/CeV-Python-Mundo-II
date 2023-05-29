''' Jogar par/impar com o pc
mostrar o nr de vitórias consecutivas do jogador
quando ele perder o jogo termina.
Escolhe um nr e o pc outro (analisa a soma de ambos)'''

from random import randint

print('~'*30)
print('PAR OU ÍMPAR? ')
print('~'*30)

jogador = int(0)
escolha = str('')
computador = int(0)
cont = 0
ganhou = 0
continuar = 'S'

while True:
    if continuar in 'Ss':
        cont += 1
        jogador = int(input('Escolha um número: '))
        escolha = str(input('[P] par ou [I] impar? ').strip().upper())
        computador = randint(1, 2)
        if ((escolha == 'P') and ((jogador+computador) % 2 == 0)) or ((escolha == 'I') and ((jogador+computador) % 2 ==1)):
            print(f'Você escolheu {escolha} e jogou {jogador}, \neu joguei {computador}, Você GANHOU!!!')
            ganhou += 1
            continuar = input('Deseja continuar? ')
            if continuar in 'Nn':
                break
        else:
            print(f'Você escolheu {escolha} e jogou {jogador}, \neu joguei {computador}, você perdeu!')
            break
print(f'Você ganhou {ganhou} vezes consecutivas!')
print('~'*30)
print(('FIM'))