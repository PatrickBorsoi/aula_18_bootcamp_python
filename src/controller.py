# Aqui ficam as funções
# Regra de negocio tbm
import requests
from db import SessionLocal, engine, Base
from models import Pokemon
from schema import PokemonSchame

Base.metadata.create_all(bind=engine)

def pegar_pokemon(pokemon_id: int) -> PokemonSchame:
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    if response.status_code == 200:
        data = response.json()
        types_list = []
        types = ', '.join(type['type']['name'] for type in data['types'])
        return PokemonSchame(name=data['name'], type=types)
    else:
        return None
    

def add_pokemon_to_db(pokemon_schema: PokemonSchame) -> Pokemon:
    with SessionLocal() as db:
        # o orm_mode = True
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon