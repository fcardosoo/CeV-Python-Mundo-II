'''Melhorar o ex061, o programa vai
perguntar quantos termos a mais o usuario
quer ver. Digitar 0 encerra o programa'''

print('-=-'*10)
print('PROGRESSÃO ARITMÉTICA')
print('-=-'*10)

primTermo = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
termo = primTermo
contador = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while contador <= total:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        contador += 1
    print('pausa')
    mais =int(input('Mais quantos termos você quer mostrar? '))
print('Prgressão finalizada com {} termos processados.'.format(total))