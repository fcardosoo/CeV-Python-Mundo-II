''' Peça 2 números ao usuário
mostre o menu [1] somar [2] mult
[3] maior [4] novos numeros [5] sair do programa'''
from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
resultado = 0
escolha = 0

while escolha != 5:
    print('Escolha uma opção: \n[1] Somar; \n[2] Multiplicar; \n[3] Maior;\n'
                        '[4] Novos números; \n[5] sair do programa.')
    escolha = int(input('Informe sua opção: '))

    if escolha == 1:
        resultado = n1 + n2
        print('O resultado da soma entre {} e {} é = {}'.format(n1, n2, resultado))
    elif escolha == 2:
        resultado = n1 * n2
        print('O resultado da multiplicação entre {} e {} é = {}'.format(n1, n2, resultado))
    elif escolha == 3:
        if n1 > n2:
            print('O valor {} é maior do que {}'.format(n1, n2))
        else:
            print('O valor {} é maior do que {}'.format(n2, n1))
    elif escolha == 4:
        n1 = int(input('Digite o valor para o primeiro número: '))
        n2 = int(input('Digite o valor para o segundo número: '))
    elif escolha == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida! Tente novamente.')
    sleep(2)
    print('=-='*10)
print('Fim do programa. Volte sempre!')