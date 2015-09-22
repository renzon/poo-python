from math import sqrt


class Vetor():
    def __init__(self, x=0, y=0):
        self.y = y
        self.x=x

    def __str__(self):
        return 'Vetor(%s, %s)'%(self.x, self.y)

    def __add__(self, other):
        return Vetor(self.x+other.x, self.y+other.y)

    def __abs__(self):
        return sqrt(self.x**2+self.y**2)



vetor=Vetor(1, 2)
vetor2=Vetor(2,2)
vetor_soma = vetor + vetor2
print(vetor_soma)
print(abs(-3))
print(abs(vetor_soma))