#Semana 1 21/03 - 28/03

#Aprendendo POO
#Self é a referência do objeto que está sendo construido em memória

class Conta: #inicio qual a classe
        def __init__(self,numero, titular, saldo,limite):   #função contrutora 
                self.numero = numero
                self.titular = titular
                self.saldo = saldo
                self.limite = limite

        def extrato(self):
                print(f'Saldo {self.saldo} do titular {self.titular}.')

        def depositar(self,valor):
                self.saldo += valor 

        def saca(self,valor):
                self.saldo -= valor


conta = Conta(123,"Ramon",1500.0,4000.0)
conta.extrato()
conta.depositar(15)
conta.extrato()
conta.saca(245)
conta.extrato()
