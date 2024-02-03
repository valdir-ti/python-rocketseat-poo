# Herança multipla é a capacidade de uma classe herdar métodos e atributos de várias classes diferentes
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def emitir_som():
        pass

class Mamifero(Animal):
    def amamentar(self):
        return (f"{self.nome} está amamentando")
    
class Ave(Animal):
    def voar(self):
        return (f"{self.nome} está voando")
    
class Morcego(Mamifero, Ave):
    def emitir_som():
        return "Morcegos emitem sons ultrassônicos"
    
morcego = Morcego(nome="Batman")

# Acessando métodos da classe base 'Animal'
print(f"Nome do morcego: {morcego.nome()}")
print(f"Som do morcego: {morcego.emitir_som()}")

# Acessando métodos da classe base 'Mamifero e Ave'
print(f"Morcego amamentando: {morcego.amamentar()}")
print(f"Morcego voando: {morcego.voar()}")
