from itertools import cycle

ciclo_2_a_9=cycle(range(2,10))

for i, valor in zip(ciclo_2_a_9, '123456789012345678901234567890'):
    print(i, valor)