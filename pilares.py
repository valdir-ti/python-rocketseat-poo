# Pilares da programação orientada a objetos
    # Herança
    # Polimorfismo
    # Encapsulamento
    # Abstração

print("\nExemplo de Herança")
# Capacidade de uma classe herdar métodos e atributos de outras classes
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"Animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "late"
    
class Gato(Animal):
    def emitir_som(self):
        return "mia"
    
dog = Cachorro(nome="Rex")
cat = Gato(nome='Felix')

print("\nExemplo de polimorfismo")
# Capacidade de um método da classe pai ser utilizado de diferentes maneiras por classes filhas diferentes entre si
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")


print("\nExemplo de encapsulamento")
# Uso de atributos privados para proteger informações da classe
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # O saldo é privado por ter dois underlines na sua atribuição
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: R${conta.consultar_saldo()}")
conta.depositar(valor=320)
print(f"Novo saldo da conta bancária = R${conta.consultar_saldo()}")
conta.depositar(valor=-100)
print(f"Novo saldo 2 da conta bancária = R${conta.consultar_saldo()}")
conta.sacar(143)
print(f"Novo saldo da conta bancária depois de sacar R$143 = R${conta.consultar_saldo()}")

print("\nExemplo de abstração")
# Funciona como um molde para outras classes, pois não podemos instanciar objetos através dela
from abc import ABC, abstractmethod

class Veiculo(ABC): # define a classe como abstrata
    
    @abstractmethod #obriga as classe filhas a adicionar esse método
    def ligar(self):
        pass

    @abstractmethod #obriga as classe filhas a adicionar esse método
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado"
    
    def desligar(self):
        return "Carro desligado"

carro_amarelo = Carro()
print(f"Carro Ligando: {carro_amarelo.ligar()}")
print(f"Carro Desligando: {carro_amarelo.desligar()}")