# Financiamento Imobiliário
# Solicitar, valor do imóvel, salário e tempo de financiamento
# Calcular o valor da parcela (s/ juros)
# Não pode exceder 30% salário. Informar se pode ou não financiar;

print('-=-'*15)
print('Tela de FINANCIAMENTO IMOBILIÁRIO')
print('-=-'*15)

i = float(input('Qual o valor do Imóvel a ser financiado? '))
t = int(input('Qual o tempo de financiamento em anos? '))
s = float(input('Qual a sua renda líquida familiar? '))
p = i/(t*12)

print('-=-'*15)
if p>(s*0.3):
    print('A pestação excedeu o limite de 30% da sua renda, infelizmente o empréstimo \033[1;31mnão será liberado!\033[m')
else:
    print('\033[1;34mEmpéstimo Liberado\033[m!!!')
    print('O valor o imóvel é R${:.2f} \nO tempo de financiamento é {} anos ou {} meses,\n'
    'Sua renda familiar é {:.2f} e sua prestação ficou R${:.2f}'.format(i, t, t*12, s, p))
print('-=-'*15)