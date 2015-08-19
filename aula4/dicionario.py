paises={'Brasil':'Português', 'Argentina':'Espanhol' }
print(paises['Argentina'])
paises.pop('Brasil')
for chave, valor in paises.items():
    print('%s : %s'%(chave, valor))

