from itertools import chain, product
from random import shuffle

NAIPES = '♢ ♠ ♡ ♣'.split()


class Carta():
  def __init__(self, numero, naipe):
    self.naipe = naipe
    self.numero = numero

  def __repr__(self):
    return 'Carta(%r, %r)' % (self.numero, self.naipe)

  def __eq__(self, other):
    return (self.numero, self.naipe) == (other.numero, other.naipe)

  def __hash__(self):
    return hash((self.numero, self.naipe))

  def __gt__(self, other):
    pesos_numeros = {str(numero): peso for peso, numero in
                     enumerate(chain(range(4, 8), 'QJKA', (2, 3)))}
    self_numero_peso = pesos_numeros[self.numero]
    outro_numero_peso = pesos_numeros[other.numero]
    if self_numero_peso == outro_numero_peso:
      pesos_naipes = {naipe: peso for peso, naipe in enumerate(NAIPES)}
      return pesos_naipes[self.naipe] > pesos_naipes[other.naipe]

    return self_numero_peso > outro_numero_peso


class Baralho():
  def __init__(self):
    numeros = chain(range(2, 8), 'J Q K A'.split())
    self._cartas = [Carta(str(numero), naipe) for numero, naipe in product(numeros, NAIPES)]

  def __repr__(self, *args, **kwargs):
    return 'Baralho(%r)' % self._cartas

  def __getitem__(self, item):
    return self._cartas[item]

  def __len__(self):
    return len(self._cartas)

  def __setitem__(self, key, value):
    self._cartas[key] = value

  def ordernar(self):
    self._cartas.sort()


baralho = Baralho()

for carta in baralho:
  print(carta)

print(baralho[-1])
print(len(baralho))

shuffle(baralho)

print(baralho)
baralho.ordernar()
print(baralho)
