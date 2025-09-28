from flask import render_template, request, redirect, url_for
from models.models_turma import banco_de_dados
from models.models_turma import Turma

class AlunoController:
     # A chamada para esse método seria feita diretamente pela classe, sem a necessidade de criar um objeto (uma instância):
     @staticmethod
     def index():
          turmas = Turma.query.all()
        #  validar pois no enunciado indica que não será usado views 
          return render_template('', turmas=turmas)
