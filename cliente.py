class Cliente():
    def __init__(self, nome, idade, peso, altura):
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura

    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome

    def getIdade(self):
        return self._idade
    def setIdade(self, idade):
        self._idade = idade

    def getPeso(self):
        return self._peso
    def setPeso(self, peso):
        self._peso = peso

    def getAltura(self):
        return self._altura
    def setAltura(self, altura):
        self._altura = altura