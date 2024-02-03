# Um decorador é uma função especial que pode ser usada para modificar ou 
# aprimorar o comportamento de outras funções ou métodos. Os decoradores 
# são uma parte poderosa e flexível do Python, proporcionando uma maneira 
# elegante de realizar tarefas comuns, como modificar argumentos ou resultados 
# de funções, medir o tempo de execução, realizar validações, entre outros.

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