from flask_sqlalchemy import SQLAlchemy

banco_de_dados = SQLAlchemy()

# inicializa a classe aluno que herda de database.Model, se tornando uma tabela dentro do banco de dados.
class Aluno(banco_de_dados.Model):

    __nome_da_tabela__ = 'alunos'
    # definindo as colunas de aluno dentro da tabela
    id = banco_de_dados.Column(banco_de_dados.Integer, primary_key=True)
    nome = banco_de_dados.Column(banco_de_dados.String(100), nullable=False)
    idade = banco_de_dados.Column(banco_de_dados.Integer, nullable=False)
    turma_id = banco_de_dados.Column(banco_de_dados.String(100), nullable=False)
    data_nascimento = banco_de_dados.Column(banco_de_dados.Date, nullable=False)
    nota_primeiro_semestre = banco_de_dados.Column(banco_de_dados.Float, nullable=False)
    nota_segundo_semestre = banco_de_dados.Column(banco_de_dados.Float, nullable=False) 