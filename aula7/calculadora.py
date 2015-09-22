class Operacao():
    def calcular(self, arg1, arg2):
        raise NotImplementedError('Deve ser implementado')


class Soma(Operacao):
    def calcular(self, arg1, arg2):
        return arg1 + arg2


class Subtracao():
    def calcular(self, arg1, arg2):
        return arg1 - arg2

class Calculadora():
    def __init__(self):
        self.arg1 = None
        self.arg2 = None
        self.sinal = None
        self.__operacoes = {}
        soma = Soma()
        self.adicionar_operacao('+',soma)
        subtracao = Subtracao()
        self.adicionar_operacao('-',subtracao)

    def obter_inputs(self):
        raise NotImplementedError('Deve ser implementado')

    def calcular_resultado(self):
        self.obter_inputs()
        operacao_selecionada=self.__operacoes[self.sinal]
        return operacao_selecionada.calcular(self.arg1, self.arg2)

    def adicionar_operacao(self, sinal, operacao):
        self.__operacoes[sinal]=operacao


class CalculadoraInfixa(Calculadora):
    def obter_inputs(self):
        self.arg1 = float(input('Digite um número: '))
        self.sinal = input('Digite o sinal da operção: ')
        self.arg2 = float(input('Digite outro número: '))


calculadora=CalculadoraInfixa()
# print(calculadora.calcular_resultado())
print(dir(calculadora))
print(calculadora._Calculadora__operacoes)