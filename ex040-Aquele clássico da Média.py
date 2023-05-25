# Pedir duas notas
#Calcular a média e informar se foi aprovado
# ou reprovado. N<5 rep; <N<6.9 média; N>7 apr

print('-=-'*15)
print('********* BOLETIM DIGITAL *********')
print('-=-'*15)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2

if m<5:
    print('Você ficou com média {}, infelizmente esta nota \n'
          'não qualifica você para passar de ano. Você\033[1;31m REPROVOU\033[m!'.format(m))
elif m<7:
    print('Você ficou com média {}, você foi\033[1:37m APROVADO!\033[m'.format(m))
else:
    print('Você ficou com média {}. PARABÉNS, você foi\033[1;32m APROVADO!!!'.format(m))
print('-=-'*20)
