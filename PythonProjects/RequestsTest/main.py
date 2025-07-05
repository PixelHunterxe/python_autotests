import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "aec6f1e6c4e62c8ae51fdc8aec219dd6"
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

body_sozdania = {
    "name": "generate",
    "photo_id": 35
}
body_izmenenia = {
    "pokemon_id": "352919",
    "name": "Гомер",
    "photo_id": 23
}

body_boi = {
    "pokemon_id": "352919"
}

'''responce = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_sozdania)
print(responce.text)''' 


"""responce_izm = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_izmenenia)
print(responce_izm.text)"""

responce_boi = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_boi)
print(responce_boi.text)

