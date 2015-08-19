lista= ['Renzo','Igor','Igor']
lista.append('Liu')
print(lista)
lista.pop(0)
print(lista)
lista2=[n+'s' for n in lista if n!='Igor']
print(lista2)
lista3=['Celso','Thalita']
lista3.extend(lista)
# print(lista3+lista)
print(lista3)
print(lista)
