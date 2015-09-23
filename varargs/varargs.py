def soma(primeiro=2, *args, **kwargs):
    print(args)
    print(kwargs)

    return primeiro + sum(args)


print(soma())
print(soma(1))
print(soma(1, 2))
print(soma(1, 2, 3))

numeros = list(range(5))
print(soma(1, *numeros, a=3, b='blah'))

dct={'a':6}
print(soma(1, *numeros, **dct))
