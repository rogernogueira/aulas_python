class Livro():
    def __init__(self, autor, titulo):
        self.autor = autor
        self.titulo = titulo
    def info(self):
        print(f"O autor do livro é {self.autor}, o titulo é {self.titulo}")


livro1 = Livro("Luciano Ramalho", "Python Fluente")
livro2 = Livro("Wes Mckinney", "Python para analise de dados")

livro1.info()
livro2.info()