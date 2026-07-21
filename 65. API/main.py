import requests, json
base_url = "https://pokeapi.co/api/v2/pokemon/"
pokemon = input("Enter a pokemon:\t").lower()

def get_pokemon(name):
    url = base_url + name
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        print("Data received")
        return response.json()
    else:
        print("Data not received")

poke_data = get_pokemon(pokemon)
if poke_data:
    # json.load(poke_data)
    print(poke_data.keys())
    print(f"Name: {poke_data["name"]}")
    print(f"ID: {poke_data["id"]}")
    print(f"Weight: {poke_data["weight"]}")
