# Pedir peso e altura e calc. IMC
#Informar se:
#até 18.5 (abaixo do peso); até 25 (ideal)
#Até 30 (sobrepeso) até 40 (obesidade)
#acima 40 morbidade

print('*'*40)
print('\033[1;33;47m****** Análise de Massa Corporal ******\033[m')
print('*'*40)

p = float(input('Informe seu peso em kilos: '))
h = float(input('Informe sua altura em metros: '))
imc= p/(h**2)

a = str('\033[1;31m abaixo do peso ideal\033[m, procure um nutricionista!')
b = str('\033[1;31m na faixa de peso ideal\033[m, PARABÉNS!')
c = str('\033[1;31mcom sobrepeso, procure um nutricionista!')
d = str('\033[1;31mcom obesidade, procure um nutricionista!')
e = str('\033[1;31mcom obesidade mórbida\033[m, procure um \033[1;31m médico\033[m!')

print('Seu peso é {}Kg, sua altura é {}m, e seu IMC é {:.2f}'.format(p, h, imc))
if imc<18.5:
    print('A análise do seu IMC índica que você está {}'.format(a))
elif imc <= 25:
    print('A análise do seu IMC indica que você está {}'.format(b))
elif imc <= 30:
    print('A análise do seu IMC indica que você está {}'.format(c))
elif imc <= 40:
    print('A análise do seu IMC indica que você está {}'.format(d))
else:
    print('A análise do seu IMC indica que você está {}'.format(e))