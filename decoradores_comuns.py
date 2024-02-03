# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # atributo da classe

    def __init__(self, nome) -> None:
        self.nome = nome # atributo de instancia
    
    # requer uma instancia pra ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
    
    @classmethod # Usado para criar instancia de uma classe
    def metodo_classe(cls):
        return f"Método de class chamado para valor={cls.valor}"
    
    @staticmethod # 
    def metodo_estatico():
        return f"Método estático não recebe referencia da classe"
    
obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())
