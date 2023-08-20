import requests
import pytest

token = '2505be46b3c3635332f1517588b5979e'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 2042})
    assert response.status_code == 200

def test_check_answer():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 2042})
    assert response.json()['trainer_name'] == 'SashaTest'
