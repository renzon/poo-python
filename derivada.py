def f():
    return 'string'


a=f

print(type(f))
print(type(a))
print(a())

def derivar(funcao, delta_x=0.000000001):
    def funcao_derivada(x):
        return (funcao(x+delta_x)-funcao(x))/delta_x

    return funcao_derivada

def reta(x):
    return x


reta_derivada=derivar(reta)

print(reta_derivada(1))
print(reta_derivada(2))

def parabola(x):
    return x**2

parabola_derivada=derivar(parabola)

print(parabola_derivada(1))
print(parabola_derivada(2))