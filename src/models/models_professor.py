from flask_sqlalchemy import SQLAlchemy

banco_de_dados = SQLAlchemy()

# inicializa a classe aluno que herda de database.Model, se tornando uma tabela dentro do banco de dados.
class Professor(banco_de_dados.Model):

    __nome_da_tabela__ = 'professores'
    # definindo as colunas de professor dentro da tabela
    id = banco_de_dados.Column(banco_de_dados.Integer, primary_key=True)
    nome = banco_de_dados.Column(banco_de_dados.String(100), nullable=False)
    idade = banco_de_dados.Column(banco_de_dados.Integer, nullable=False)
    materia = banco_de_dados.Column(banco_de_dados.String(100), nullable=False)
    observacoes = banco_de_dados.Column(banco_de_dados.Text, nullable=True)