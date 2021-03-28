#Semana 1 21/03 - 28/03

class Conta: #inicio qual a classe
        def __init__(self,numero, titular, saldo,limite):   #função contrutora 
                self.__numero = numero
                self.__titular = titular
                self.__saldo = saldo
                self.__limite = limite

        @property
        def extrato(self):
                print(f'Saldo {self.__saldo} do titular {self.__titular}.')

        def depositar(self,valor):
                self.__saldo += valor 

        def __pode_sacar(self,valor):
                valor_disponivel = self.__saldo + self.__limite
                return valor <= valor_disponivel

        def saca(self,valor):
                if self.__pode_sacar(valor):
                        self.__saldo -= valor
                else:
                        print(f'O valor {valor} ultrapassou o limite.')
        
        def transfere(self,valor,destino):
                self.saca(valor)
                destino.depositar(valor)
        
        @property  # serve para quando chamar o método não precisar colocar (). Mas só serve p/metodos sem valor
        def acessa_saldo(self):
                return self.__saldo

        @property
        def acessa_titular(self):
                return f'O titular da conta de numero {self.__numero} é o {self.__titular}'


conta = Conta(123,"Ramon",1500.0,400.0)
conta2 = Conta(234,"Bruno",1200,2000)
conta.saca(4000)
print(conta.acessa_titular)



"""Conceito aprendido:

   Atualmente, conseguimos mudar o valor dos atributos da nossa classe. Por exemplo, conseguimos mudar o saldo da conta simplemente atribuindo um valor a ele:

   conta.saldo = 10000  #Isso é um problema, pois estamos alterando diretamente o saldo.

   O saldo da conta só deve ser alterado com os métodos deposita e saca.Então para resolvermos este problema, torne - os privados, ou seja, adicionando 2 underscores à frente dos atributos:

   def __init__(self, numero, titular, saldo, limite):
    print("Construindo objeto ... {}".format(self))
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite



#Mais uma ponderação sobre classes:

   uma classe deve ter apenas uma responsabilidade (ou deve ter apenas uma razão para existir). Em outras palavras, ela não deve assumir responsabilidades que não são delas.(princípio de responsabilidade única)
"""

#Aula proprieda (@property)

'''class Cliente:
        def __init__(self,nome):
                self.__nome = nome
        
        @property
        def nome(self):
                return self.__nome.title()

        @nome.setter
        def nome(self,nome):
                self.__nome = nome


cliente= Cliente("Ramon")
print(cliente.nome)
cliente.nome = "Bruna"
print(cliente.nome)'''


''' O python segue uma convenção para deixar atributos e métodos privados, por exemplo:
           def __init__(self,nome,numero_conta):
                   self.__nome = nome
                   self.__numero_conta = numero_conta
    se você perceber, colocamos 2 undescors antes do atributo. Se você chamar o atributo, o python avisa que aquele atributo é privado.
    Também é possível fazer isso com método, por exemplo:
           def __nomed0método(self):
                   -o que irá fazer-

É importante obser, pois, quando dentro da classe você for chamar o método caso seja necessário, é preciso chamar com os dois undercors. Mas não será possivel o usuário chamar esse método. '''

