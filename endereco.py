class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado

    def getRua(self):
        return self._rua
    def setRua(self, rua):
        self._rua = rua

    def getNumero(self):
        return self._numero
    def setNumero(self, numero):
        self._numero = numero

    def getBairro(self):
        return self._bairro
    def setBairro(self, bairro):
        self._bairro = bairro

    def getCidade(self):
        return self._cidade
    def setCidade(self, cidade):
        self._cidade = cidade

    def getEstado(self):
        return self._estado
    def setEstado(self, estado):
        self._estado = estado