def calcular():
    argumento_1 = float(input('Digite um número: '))
    sinal = input('Digite o sinal da operção: ')
    argumento_2 = float(input('Digite outro número: '))
    if sinal == '+':
        return argumento_1+argumento_2
    elif sinal == '-':
        return argumento_1-argumento_2
    else:
        raise Exception('Operação não implementada')

if __name__=='__main__':
    print(calcular())