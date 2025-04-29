import requests
import warnings
warnings.filterwarnings("ignore")
def get_pokemon_weight(pokemon_name):
    """
    Fetches the weight of a given Pokémon from the PokéAPI.
    
    :param pokemon_name: Name of the Pokémon (case-insensitive).
    :return: Weight of the Pokémon in hectograms (hg) or an error message.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    response = requests.get(url,verify=False)
    
    if response.status_code == 200:
        data = response.json()
        weight = data.get("weight", "Unknown")
        return {"text_description" : f"{pokemon_name.capitalize()} weighs {weight} hectograms ({weight / 10} kg)."}
    else:
        return f"Pokémon '{pokemon_name}' not found!"

if __name__ == "__main__":
    # Example usage
    print(get_pokemon_weight("charizard"))
    print(get_pokemon_weight("pikachu"))
    print(get_pokemon_weight("gyarados"))
    print(get_pokemon_weight("psyduck"))