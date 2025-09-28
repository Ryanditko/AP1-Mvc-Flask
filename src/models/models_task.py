from models import banco_de_dados
from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class ModelsTask: 
    __nome_da_tabela__ = "tasks"

    #TODO definir as colunas da tabela tasks 