import json
import os
import settings
from pokeapi import get_pokemon_data


def get_stats_from_data(data):
    stats = {}
    for item in data["stats"]:
        stat_name = item["stat"]["name"]
        stats[stat_name] = item["base_stat"]
    return stats


def save_stats(all_stats):
    with open(settings.STATS_FILE, "w") as file:
        json.dump(all_stats, file, indent=4)


def load_stats():
    all_stats = {}
    if os.path.exists(settings.STATS_FILE):
        with open(settings.STATS_FILE) as file:
            all_stats = json.load(file)

    something_added = False
    for name in settings.POKEMON_NAMES:
        if name not in all_stats:
            data = get_pokemon_data(name)
            if data is not None:
                all_stats[name] = get_stats_from_data(data)
                something_added = True
                print(f"Stats ready: {name}")

    if something_added:
        save_stats(all_stats)

    return all_stats
