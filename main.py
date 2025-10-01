# criando uma pathlib para facilitar o uso em outros sistemas operacionais
from pathlib import Path
arquivo_src = Path(__file__).parent / "src"

import os
from flask import Flask
from config import Config
from models import banco_de_dados
from flasgger import Swagger
from api.professores.api_professores import rotas_professores

# TODO configurar a aplicação flask aqui abaixo (sem a necessidade de views/html para a aplicação)
app = Flask(__name__)
app.config.from_object(Config)

# iniciando o banco de dados 
banco_de_dados.init_app(app)

swagger = Swagger(app, template_file='docs/swagger.yaml')

with app.app_context():
    banco_de_dados.create_all()

rotas_professores(app)

if __name__ == '__main__':
    app.run(debug=True)