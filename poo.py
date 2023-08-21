class Pessoa():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo= sexo
    def saudacao(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos")

class Professor(Pessoa):
    def __init__(self, nome, idade , sexo, titulo):
        super().__init__(nome, idade, sexo)
        self.titulo=titulo
    def info(self):
        print(f"O titulo é {self.titulo}")
prof_1 = Professor("Manoel", "65", "Masculino", "Doutor")
print(prof_1.nome)
print(prof_1.saudacao())






