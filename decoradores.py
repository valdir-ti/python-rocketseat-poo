# Decoradores adicionam funcionalidades nas funções sem alterar o comportamento delas, 
# através de wrapper, que são os encapsulamentos da função com códigos antes de depois da mesma

# função
def meu_decorador(func):
    def wrapper():
        print("\nAntes da função ser chamada")
        func()
        print("Depois da função ser chamada\n")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")
minha_funcao()


#classe
from typing import Any
class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("\nAntes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)\n")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Minha segunda função foi chamada")

segunda_funcao()