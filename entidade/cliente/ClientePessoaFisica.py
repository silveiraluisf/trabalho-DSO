from entidade.cliente.abstractCliente import AbstractCliente
from entidade.veiculo.veiculo import Veiculo
 
class ClientePessoaFisica(AbstractCliente):
     
    def __init__(self, codigo: int, nome: str, telefone: int, endereco: str,
                 data_nascimento: str, cpf: str, rg: str, orgao_emissor: str, veiculo: Veiculo):
         super().__init__(codigo, nome, telefone, endereco)
         self.__data_nascimento = data_nascimento
         self.__cpf = cpf
         self.__rg = rg
         self.__orgao_emissor = orgao_emissor
         self.__veiculo = veiculo

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: str):
        if isinstance(data_nascimento, str):
            self.__data_nascimento = data_nascimento
            
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.cpf = cpf

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg: str):
        if isinstance(rg, str):
            self.rg = rg

    @property
    def orgao_emissor(self):
        return self.__orgao_emissor
    
    @orgao_emissor.setter
    def orgao_emissor(self, orgao_emissor: str):
        if isinstance(orgao_emissor, str):
            self.__orgao_emissor = orgao_emissor

    @property
    def veiculo(self):
        return self.__veiculo
 
    @veiculo.setter
    def veiculo(self, veiculo: Veiculo):
        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo

