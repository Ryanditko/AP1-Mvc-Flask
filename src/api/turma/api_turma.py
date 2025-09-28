# realizar o CRUD de turmas aqui
from flask import render_template, request, redirect, url_for
from models.models_turma import banco_de_dados
from models.models_turma import Turma

class TurmaApi:

    @staticmethod
    def TurmaPost():
        if request.method == 'POST':
              pass 
        
    # TODO implementar os outros métodos aqui abaixo