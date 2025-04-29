from langchain.tools import Tool
from tools.pokemon_api import get_pokemon_weight
import json

def fetch_weights(pokemons_json: str) -> str:
    pokemons = json.loads(pokemons_json)
    
    weights = {}
    for human, pokes in pokemons.items():
        weights[human] = []
        for poke in pokes:
            result = get_pokemon_weight(poke)
            weight_str = result["text_description"].split("weighs")[1]
            weight_kg = float(weight_str.split("(")[1].replace("kg).", "").strip())
            weights[human].append((poke, weight_kg))
    return str(weights)

fetch_weights_tool = Tool(
    name="fetch_weights",
    description="Fetch Pokémon weights for two humans",
    func=fetch_weights,
)