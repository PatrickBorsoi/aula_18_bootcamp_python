#Cuida do meu banco
#Criar tabelas, atualizar, regras de validações

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base


class Pokemon(Base):
    __tablename__ = 'pokemons' # Nome da tabela
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    created_at = Column(DateTime, default=func.now())