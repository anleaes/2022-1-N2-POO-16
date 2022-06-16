class CadastroCliente:
    def __init__(self, cpf, endereco, telefone, nome):
        self._cpf = cpf
        self._endereco = endereco
        self._telefone = telefone
        self._nome = nome

    def getCPF(self):
        return self._cpf
    def setCPF(self, cpf):
        self._cpf = cpf

    def getEndereco(self):
        return self._endereco
    def setEndereco(self, endereco):
        self._endereco = endereco

    def getTelefone(self):
        return self._telefone
    def setTelefone(self, telefone):
        self._telefone = telefone

    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome

    def cadastroNaoConfirmado(self):
        return print("ESTE CADASTRO NAO FOI CONFIRMADO")

    def verificaCadastro(self, nome, cpf, endereco, telefone):
        if self.getNome() is not None and self.getNome() is nome:
            if self.getCPF() is not None and self.getCPF() > 0 and self.getCPF() is cpf:
                if self.getEndereco() is not None and self.getEndereco() is endereco:
                    if self.getTelefone() is not None and self.getTelefone() is telefone:
                        self.setNome(nome)
                        self.setCPF(cpf)
                        self.setEndereco(endereco)
                        self.setTelefone(telefone)
                        print(f"nome: {nome.getNome()} CONFIRMADO")
                        self._cadastro = True
                    else:
                        self.cadastroNaoConfirmado()
                else:
                    self.cadastroNaoConfirmado()
            else:
                self.cadastroNaoConfirmado()
        else:
            self.cadastroNaoConfirmado()