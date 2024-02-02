class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos"

pessoa1 = Pessoa("João", 33)
pessoa2 = Pessoa("Maria", 13)

mensagem1 = pessoa1.saudacao()
mensagem2 = pessoa2.saudacao()

print(mensagem1)
print(mensagem2)