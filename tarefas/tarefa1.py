def quadrado_menores(n):
    return [i ** 2 for i in range(1, n + 1) if i ** 2 <= n]
    # lst = []
    # for i in range(1, n+1):
    #     quadrado = i ** 2
    #     if quadrado <= n:
    #         lst.append(quadrado)
    #     else:
    #         return lst
    # return lst


assert [1] == quadrado_menores(1)
assert [1, 4] == quadrado_menores(4)
assert [1, 4, 9] == quadrado_menores(9)
assert [1, 4, 9] == quadrado_menores(11)


def soma_quadrados(n):

    if n > 0:
        menores = quadrado_menores(n)
        ultimo = menores[-1]
        if ultimo == n:
            return [n]
        else:
            lista=[ultimo]
            n-=ultimo
            lista.extend(soma_quadrados(n))
            return lista

    return[0]

assert [0] == soma_quadrados(0)
assert [1] == soma_quadrados(1)
assert [4] == soma_quadrados(4)
assert [9] == soma_quadrados(9)
assert [1,1] == soma_quadrados(2)
assert [1,1,1] == soma_quadrados(3)
assert [4,1] == soma_quadrados(5)
assert [4,4,4] == soma_quadrados(12)

