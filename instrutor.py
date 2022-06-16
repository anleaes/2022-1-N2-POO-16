class Instrutor():
    def __init__(self, nome, cliente, especialidade):
        self._nome = nome
        self._cliente = cliente
        self._especialidade = especialidade

    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome


    def getCliente(self):
        return self._cliente
    def setCliente(self, cliente):
        self._cliente = cliente

    def getEspecialidade(self):
        return self._especialidade
    def setEspecialidade(self, especialidade):
        self._especialidade = especialidade