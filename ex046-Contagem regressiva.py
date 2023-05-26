# Faça contagem de 10 a zero com 1seg de intervalo

import time

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('Fim')