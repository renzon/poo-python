lista=enumerate('zero um dois tres quatro cinco seis sete oito nove'.split(' '))
numero_string=dict(lista)
string_numero={valor:chave for chave, valor in numero_string.items()}
print(string_numero)


def para_numeral(n):
    numeros = [numero_string[int(digito)] for digito in str(n)]
    return ', '.join(numeros)


assert "um" == para_numeral(1)
assert "um, dois" == para_numeral(12)
assert "um, um" == para_numeral(11)






def para_inteiro(string_n):
    n_lista=[str(string_numero[digito]) for digito in string_n.split(', ')]

    return int(''.join(n_lista))


assert 1==para_inteiro('um')
assert 12==para_inteiro('um, dois')