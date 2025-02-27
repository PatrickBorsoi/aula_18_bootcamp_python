from pydantic import BaseModel

class PokemonShame(BaseModel): # Contrato de dados, Schema de dados, View da API
    name: str
    type: str

    class Config:
        #Ler sobre
        orm_mode = True