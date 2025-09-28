from flask_sqlalchemy import SQLAlchemy

banco_de_dados = SQLAlchemy()

# inicializa a classe aluno que herda de database.Model, se tornando uma tabela dentro do banco de dados.
class Turma(banco_de_dados.Model):

    __nome_da_tabela__ = 'turmas'
    # definindo as colunas de turma dentro da tabela
    id = banco_de_dados.Column(banco_de_dados.Integer, primary_key=True)
    nome = banco_de_dados.Column(banco_de_dados.String(100), nullable=False)
    professor_id = banco_de_dados.Column(banco_de_dados.Integer, nullable=False)
    ativo = banco_de_dados.Column(banco_de_dados.Boolean, default=True)