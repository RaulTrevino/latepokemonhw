import requests

def evolve_pokemon(pokemon_name):
    # Fetch data from the PokéAPI
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/')

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data for {pokemon_name}.")
        return

    data = response.json()

    # Check if the Pokémon can evolve further
    if 'evolves_to' in data.get('species', {}).get('evolves_from_species', {}):
        evolves_to = data['species']['evolves_from_species']['name']
        print(f"{pokemon_name} can evolve into {evolves_to}.")
    else:
        print(f"{pokemon_name} can't evolve further.")

# Example usage:
evolve_pokemon('weedle')
