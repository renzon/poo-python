try:
    1/1
    print('Depois da excecao de divisão por 0')
except ZeroDivisionError :
    print('Tratando qualquer excecao')
else:
    print('Executado se não houver erro')
finally:
    print('Sempre é executado')