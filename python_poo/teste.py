from conta import Conta
from cliente import Cliente

conta1 = Conta(123,"Felipe", 1000000000000,1000000000000)
conta2 = Conta(321,"Luciana", 1000000000000,1000000000000)
conta1.extrato()

valor = 10.0
conta1.sacar(valor)
conta1.extrato()
conta2.depositar(valor)
conta2.extrato()


conta1.transferir(valor,conta2)
conta1.extrato()
conta2.extrato()

cliente1 = Cliente('felipe Janser')
print(cliente1.get_nome())

