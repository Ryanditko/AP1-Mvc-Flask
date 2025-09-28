# realizar o CRUD de alunos aqui
from flask import render_template, request, redirect, url_for
from models.models_aluno import banco_de_dados
from models.models_aluno import Aluno

class AlunoApi:

    @staticmethod
    def AlunoPost():
        if request.method == 'POST':
              pass 
        
    # TODO implementar os outros métodos aqui abaixo