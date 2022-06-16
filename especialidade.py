class Especialidade:
    def __init__(self, nome, instrutor):
        self._nome = nome
        self._instrutor = instrutor

    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome

    def getInstrutor(self):
        return self._instrutor
    def setInstrutor(self, instrutor):
        self._instrutor = instrutor