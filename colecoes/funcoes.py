from itertools import chain, product, permutations, combinations, cycle

r10 = range(10)
r0 = range(9, 0, -1)
cadeia = chain(r10, r0)
print(list(cadeia))

paises = ['Brasil', 'Estados Unidos', 'Japão']
linguas = ['Portugues', 'Ingles', 'Japones', 'Blah']

for pais, lingua in zip(paises, linguas):
  print(pais, lingua)

paises_dct = dict(zip(paises, linguas))
print(paises_dct)

numeros = range(2, 11)
naipes = '♣ ♡ ♠ ♢'.split()

for n in numeros:
  for naipe in naipes:
    print(n, naipe)

for carta in product(numeros, naipes):
  print(carta[0], carta[1])

for combinacao in permutations('ABC', 2):
  print(combinacao)

print('Combinações')

for combinacao in combinations('ABC', 2):
  print(combinacao)

ciclo = cycle('ABC')

for i, letra in zip(range(12), ciclo):
  print(i, letra)

numeros = range(10)

# lista=[]
# for valor in numeros:
#   if valor%2==0:
#     lista.append(valor **2)

lista = [valor ** 2 for valor in numeros if valor % 2 == 0]

print(lista)
