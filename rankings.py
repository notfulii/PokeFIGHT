import json
import os
import settings


def load_rankings():
    if not os.path.exists(settings.RANKINGS_FILE):
        return []

    with open(settings.RANKINGS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_rankings(records):
    folder = os.path.dirname(settings.RANKINGS_FILE)
    os.makedirs(folder, exist_ok=True)

    with open(settings.RANKINGS_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


def get_time(record):
    return record["time"]


def add_record(record):
    records = load_rankings()
    records.append(record)
    records.sort(key=get_time)

    best_records = records[:settings.RANKING_SIZE]
    save_rankings(best_records)


def format_time(total_seconds):
    total_seconds = int(total_seconds)
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    if seconds < 10:
        return f"{minutes}:0{seconds}"
    return f"{minutes}:{seconds}"
