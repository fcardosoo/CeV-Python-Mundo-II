# ler 6 numeros e mostrar apenas
# a soma dos pares

soma = 0
cont = 0
par = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        soma += n
        par += 1
    cont += 1
print('Você informou {} valores, sendo {} valores pares e a soma \ndos números pares é: {}'.format(cont, par,soma))
