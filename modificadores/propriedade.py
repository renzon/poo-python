class Base():
    def __init__(self):
        self.__quantidade = 0;

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, value):
        if(value>=0):
            self.__quantidade=value


b = Base()
b.quantidade=-3
print(b.quantidade)
