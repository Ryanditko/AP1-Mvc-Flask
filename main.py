# criando uma pathlib para facilitar o uso em outros sistemas operacionais
from pathlib import Path
arquivo_src = Path(__file__).parent / "src"

import os
from flask import app, flask
from config import Config

# TODO configurar a aplicação flask aqui abaixo (sem a necessidade de views/html para a aplicação)
app.config.from_object(Config)

# iniciando o banco de dados 
