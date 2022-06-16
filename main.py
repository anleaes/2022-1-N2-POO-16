from instrutor import Instrutor
from unidade import Unidade
from especialidade import Especialidade
from cliente import Cliente
from cadastroCliente import Cadastrocliente
from endereco import Endereco
from telefone import Telefone

cliente1 = Cliente("Joao", 19, 60, 180)

endereco1 = Endereco("Rua dos Andradas", 55, "centro", "Porto Alegre", "RS")

telefone1 = Telefone(51, 33335555)

unidade1 = Unidade("Centro", endereco1, telefone1)

unidade1 = Unidade(1, 1, unidade1)

cadastroP1 = CadastroCliente(123456789, endereco1, telefone1,cliente1)

instrutor1 = Instrutor("Rafael",cliente1)

especialidade1 = Especialidade("Ganho de Massa", instrutor1)


