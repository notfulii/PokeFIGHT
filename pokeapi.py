import json
import os
import requests
import settings


def get_pokemon_data(name):
    os.makedirs(settings.FOLDER_DATA, exist_ok=True)
    path = f"{settings.FOLDER_DATA}/{name.lower()}.json"

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    url = settings.POKEMON_URL + name.lower()
    response = requests.get(url, timeout=settings.REQUEST_TIMEOUT)

    if response.status_code != 200:
        print(f"Pokémon '{name}' not found")
        return None

    data = response.json()
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file)
    return data


def get_move_data(name):
    url = settings.MOVE_URL + name
    response = requests.get(url, timeout=settings.REQUEST_TIMEOUT)

    if response.status_code != 200:
        print(f"Move '{name}' not found")
        return None

    return response.json()
