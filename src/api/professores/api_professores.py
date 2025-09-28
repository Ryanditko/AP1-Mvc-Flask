# realizar o CRUD de professores aqui
from flask import render_template, request, redirect, url_for
from models.models_professor import banco_de_dados
from models.models_professor import Professor

class ProfessorApi:

    @staticmethod
    def ProfessorPost():
        if request.method == 'POST':
              pass  
         
    # TODO implementar os outros métodos aqui abaixo   