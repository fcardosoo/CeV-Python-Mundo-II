# Condições Aninhadas

#Condição SIMPLES
nome = str(input('Qual o seu nome? '))
if nome == 'Fabiano':
    print('Que nome bonito!')
print('Tenha um bom dia, {}!'.format(nome))
print('*'*30)

#Condição Composta - Estrutura ANINHADA
n = str(input('Qual o seu nome? '))
if n == 'Fabiano':
    print('Que nome bacana!')
elif n == 'Pedro' or n == 'Maria' or n == 'Lucas':
    print('Seu nome é bíblico!')
elif n in 'Aline Laura Chloe':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(n))
print('*'*30)
