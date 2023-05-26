# Ler o primeiro termo e a razão
# de uma PA e mostrar os 10 primeiros
# termos desta PA

print('='*35)
print('OS 10 PRIMEIROS TERMOS DE UMA P.A.')
print('='*35)

i = int(input('Informe o termo inicial: '))
r = int(input('Informe a razão da PA: '))
decimoTermo = i +(10-1)*r
for c in range(i, decimoTermo+r, r):
    print('{}'.format(c), end = ' -> ')
    i += r
print('Acabou!')