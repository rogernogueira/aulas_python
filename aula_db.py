import sqlite3

conexao = sqlite3.connect("aula.db")

conexao.execute('''CREATE TABLE IF NOT EXISTS aluno
                ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INT NOt NULL); ''')

def cria_aluno(conexao, nome, idade): 
    novo_aluno = conexao.execute("INSERT INTO aluno(nome, idade) VALUES (?,?);", (nome,idade));
    conexao.commit()
    print("Aluno cadastrado")
    return novo_aluno

def listar_alunos(conexao):
    alunos = conexao.execute("SELECT * FROM aluno;").fetchall()
    for aluno in alunos:
        print(aluno)
    return alunos
    
def atualizar_aluno(conexao, id, novo_nome, nova_idade):
    aluno_atualizado = conexao.execute("UPDATE aluno SET nome = ?, idade = ? WHERE id = ?;", (novo_nome, nova_idade,id)).fetchall()
    conexao.commit()
    return aluno_atualizado

def delete_aluno(conexao,id):
    conexao.execute("DELETE FROM aluno WHERE id = ?;",(id,))
    conexao.commit()
    print("Aluno deletado corretamente")
