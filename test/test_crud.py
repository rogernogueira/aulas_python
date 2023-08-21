import unittest
import sqlite3
from aula_db import cria_aluno, listar_alunos, atualizar_aluno,delete_aluno


class TestCrud(unittest.TestCase):
    def setUp(self):
        self.conexao = sqlite3.connect(":memory:")
        self.conexao.execute('''CREATE TABLE IF NOT EXISTS aluno
                ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INT NOt NULL); ''')

    def tearDown(self):
        self.conexao.close()


    def test_cria_aluno(self):
        cria_aluno(self.conexao, "Roger",12)
        cria_aluno(self.conexao, "Manoel",68)
        alunos  = self.conexao.execute("SELECT * FROM aluno").fetchall()
        self.assertEqual(len(alunos),2)
        self.assertEqual(alunos[0][1], "Roger")

    def test_lista_aluno(self):
        cria_aluno(self.conexao, "Roger",12)
        cria_aluno(self.conexao, "Manoel",68)
        alunos = listar_alunos(self.conexao)
        self.assertEqual(len(alunos), 2)
        
    def test_atualizar_aluno(self):
        cria_aluno(self.conexao, "Roger",12)
        cria_aluno(self.conexao, "Manoel",68)
        atualizar_aluno(self.conexao,1, "Rogério Nogueira", "27" )
        aluno = self.conexao.execute("SELECT * FROM aluno WHERE id = ? ", (1,)).fetchone()
        self.assertEqual(aluno[1], "Rogério Nogueira")


    def test_deletar_aluno(self):
        cria_aluno(self.conexao, "Roger",12)
        cria_aluno(self.conexao, "Manoel",68)
        delete_aluno(self.conexao,1)
        alunos = self.conexao.execute("SELECT * FROM aluno").fetchall()
        self.assertEqual(len(alunos), 1)
        self.assertEqual(alunos[0][1], "Manoel")
    
        
    



