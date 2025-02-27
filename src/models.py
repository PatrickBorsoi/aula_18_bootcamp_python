from sqlalchemy import Collumn, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base


class Pokemon(Base):
    __tablename__ = 'pokemons' # Nome da tabela
    id = Collumn(Integer, primary_key=True, index=True)
    name = Collumn(String)
    type = Collumn(String)
    created_at = Collumn(DateTime, default=func.now())