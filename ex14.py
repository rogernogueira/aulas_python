class Autor():
    def __init__ (self, nome):
        self.nome = nome

class Livro():
    def __init__(self,titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def emprestar(self):
        if self.emprestado == False:
            self.emprestado = True
        else:
            print ("Livro  já emprestado")
        
    def devolver(self,):
        if self.emprestado ==True:
            self.emprestado = False 
        else:
            print("Livro ja  devolvido")
    
class Usuario():
    def __init__(self, login):
        self.login = login

autor_1 = Autor("Wes Mckinney")
livro_1 = Livro(" Python para analise de dados", autor_1)


livro_1.emprestar()
print(autor_1.nome)
print(livro_1.titulo)
print(livro_1.emprestado)
livro_1.emprestar()