# LAÇOS, REPETIÇÕES E ITERAÇÕES

# 1ª) Estrutura - Laço com estrutura de controle
i = int(input('Digite o número incial: '))
f = int(input('Digite o número final: '))
p = int(input('Digite o passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')

# solitando valores e apresentando um somatório

s = 0

for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório dos valores foi {}.'.format(s))