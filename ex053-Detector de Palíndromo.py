# ler uma frase e informar se ela é um palíndromo

print('*'*35)
print('PALINDROMOS')
print('*'*35)

frase = str(input('Digite uma frase: ')).strip().upper()
#print('Você digitou a frase {}'.format(frase))

palavras = frase.split()
#print(palavras)
junto = ''.join(palavras)
#print(junto)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
#print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')