import json
import os
import settings
from pokeapi import get_pokemon_data, get_move_data


def get_level(move):
    return move["level"]


def get_move_names(data):
    level_up_moves = []
    other_names = []

    for item in data["moves"]:
        name = item["move"]["name"]
        highest_level = -1

        for detail in item["version_group_details"]:
            if detail["move_learn_method"]["name"] == "level-up":
                if detail["level_learned_at"] > highest_level:
                    highest_level = detail["level_learned_at"]

        if highest_level == -1:
            other_names.append(name)
        else:
            level_up_moves.append({"name": name, "level": highest_level})

    level_up_moves.sort(key=get_level, reverse=True)

    names = []
    for move in level_up_moves:
        names.append(move["name"])
    for name in other_names:
        names.append(name)
    return names


def choose_moves(data):
    chosen = []

    for name in get_move_names(data):
        move_data = get_move_data(name)
        if move_data is None or move_data["power"] is None:
            continue

        move = {
            "name": name,
            "power": move_data["power"],
            "type": move_data["type"]["name"],
            "damage_class": move_data["damage_class"]["name"]
        }
        chosen.append(move)

        if len(chosen) == settings.MOVES_PER_POKEMON:
            break

    if len(chosen) == 0:
        chosen.append(settings.BACKUP_MOVE)

    return chosen


def save_moves(all_moves):
    with open(settings.MOVES_FILE, "w") as file:
        json.dump(all_moves, file, indent=4)


def load_moves():
    all_moves = {}
    if os.path.exists(settings.MOVES_FILE):
        with open(settings.MOVES_FILE) as file:
            all_moves = json.load(file)

    something_added = False
    for name in settings.POKEMON_NAMES:
        if name not in all_moves:
            data = get_pokemon_data(name)
            if data is not None:
                all_moves[name] = choose_moves(data)
                something_added = True
                print(f"Moves ready: {name}")

    if something_added:
        save_moves(all_moves)

    return all_moves
