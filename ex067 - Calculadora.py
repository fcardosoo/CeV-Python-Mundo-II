''' Tabuada. Continuar? Interromper quando usuario entrar com numero negativo.'''

print('~~~~~~~ CALCULADORA ~~~~~~~')

n = int(0)
c = 1

while True:
    n = int(input('Escolha um número POSITIVO \npara mostrar a tabuada: '))
    if n < 0:
        break
    print('~' * 27)
    for c in range(1, 11):
        print(f'{n:3} x {c:3} = {n*c:3}')
    print('~' * 27)
    c += 1

print('~'*27)
print('Tabuada encerrada!')