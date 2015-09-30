class Pessoa():
    OLHOS = 2
    def __init__(self, nome):
        print('Iniciando __init__ de Pessoa')
        self.nome=nome

    def cumprimentar(this):
        return 'Olá, meu nome é %s'%this.nome

    def __eq__(self, other):
        return self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)

    def __repr__(self):
        return 'Pessoa(%s)'%self.nome

pessoa = Pessoa('Renzo')
denis = Pessoa('Denis')

print(pessoa.nome)
print(denis.nome)
print(denis.cumprimentar())
print(denis.cumprimentar())
print(pessoa.cumprimentar())
denis.OLHOS = 3
Pessoa.OLHOS=4
print(Pessoa.OLHOS)
print(pessoa.OLHOS)
print(denis.OLHOS)
del denis.OLHOS
print(denis.OLHOS)