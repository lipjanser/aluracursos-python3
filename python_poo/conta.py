
class Conta:
    
    def __init__(self, numero, titular, saldo, limite) -> None:
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}.".format(self.__saldo,self.__titular))
    
    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Saldo + Limite insuficiente na conta! R$ {}".format(self.__saldo + self.__limite))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237', 'Santander':'033', 'Itaú': '341'}


class ContaCorrente(Conta):
    
    def __init__(self, numero, titular, saldo, limite,juros_cheque_especial) -> None:
        super().__init__(numero,titular,saldo,limite)
        self.juros_cheque_especial = juros_cheque_especial
        
class ContaPoupanca(Conta):
    
    def __init__(self, numero, titular, saldo, limite,data_aniversario) -> None:
        super().__init__(numero,titular,saldo,limite)
        self.data_aniversario = data_aniversario
