import requests

token = '2505be46b3c3635332f1517588b5979e'
host = 'https://api.pokemonbattle.me:9104'

response = requests.post(f'{host}/pokemons', json = {
    "name": "Автотест",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type': 'application/json', 'trainer_token' : token})

print(response.text)

response_change_name = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6343",
    "name": "Автотест2",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type': 'application/json', 'trainer_token' : token})

print(response_change_name.text)

response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6343"
}, headers = {'Content-Type': 'application/json', 'trainer_token' : token})

print(response_add_pokeball.text)



