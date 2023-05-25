#complementar o ex035
#Além de informar se 3 segmentos de reta pode formar um triângulo
#Informar o tipo de triângulo
# 3 lados iguais - equilátero
# 2 lados iguais - Isósceles
# nenhum lado igual - escaleno

print('-=-'*10)
print('Analisando TRIÂNGULOS!!!')
print('-=-'*10)

r = float(input('Informe o valor da reta 1: '))
s = float(input('Informe o valor da reta 2: '))
t = float(input('Informe o valor da reta 3: '))

if r<(s+t) and s<(r+t) and t<(r+t):
    print('*'*35)
    print('É possível formar um triângulo!')

    if r == s == t:
        print('Este triângulo é equilátero!')
    elif r != s != t != r:
        print('Este triângulo é escaleno!')
    else:
        print('Este triângulo é isósceles!')

    print('*' * 35)
else:
    print('*' * 35)
    print('Não é possível formar um triângulo!')
    print('*' * 35)
