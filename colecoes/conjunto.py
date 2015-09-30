from aula6.pessoas_tipos import Homem, Mulher

if __name__ == '__main__':
    renzo = Homem('Renzo')
    renzo_igual = Homem('Renzo')
    renzo_identico = renzo
    barbara = Mulher('Barbara')
    igor = Homem('Igor')
    print(id(renzo))
    print(id(renzo_identico))
    print(id(renzo_igual))
    print(renzo is renzo_igual)
    print(renzo is renzo_identico)
    print(renzo == renzo_igual)
    print(renzo == renzo_identico)

    conjunto=set((renzo, renzo_identico, renzo_igual, barbara))
    conjunto2=set((igor, barbara))
    print(conjunto)
    print('Acabou')
    print(renzo in conjunto)
    print(renzo in conjunto2)
    print(conjunto.union(conjunto2))
    print(conjunto.difference(conjunto2))
    print(conjunto.intersection(conjunto2))
    print(conjunto)
