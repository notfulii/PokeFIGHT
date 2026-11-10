import os
import pygame
import requests
import settings
import sound
from pokeapi import get_pokemon_data
from pokemon import Pokemon
from animation import load_gif
from stats import load_stats
from moves import load_moves


def download_file(url, path):
    if os.path.exists(path):
        return path
    if url is None:
        return None

    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)

    response = requests.get(url, timeout=settings.REQUEST_TIMEOUT)
    with open(path, "wb") as file:
        file.write(response.content)

    print(f"Downloaded: {path}")
    return path


def load_sprite(path, max_size):
    image = pygame.image.load(path)

    visible_area = image.get_bounding_rect()
    image = image.subsurface(visible_area).copy()

    biggest_side = max(image.get_width(), image.get_height())
    factor = max_size / biggest_side
    new_width = int(image.get_width() * factor)
    new_height = int(image.get_height() * factor)

    image = pygame.transform.scale(image, (new_width, new_height))
    return image.convert_alpha()


def load_frames(gif_path, png_path, max_size):
    if gif_path is not None:
        return load_gif(gif_path, max_size)
    if png_path is None:
        return None

    image = load_sprite(png_path, max_size)
    return [{"image": image, "time": settings.STILL_FRAME_TIME}]


def flip_frames(frames):
    for frame in frames:
        frame["image"] = pygame.transform.flip(frame["image"], True, False)
    return frames


def load_pokemon(name, all_stats, all_moves):
    data = get_pokemon_data(name)
    if data is None:
        return None

    sprites = data["sprites"]
    animated = sprites["versions"]["generation-v"]["black-white"]["animated"]
    file_name = name.lower()

    front_png = download_file(sprites["front_default"], f"{settings.FOLDER_FRONT}/{file_name}.png")
    back_png = download_file(sprites["back_default"], f"{settings.FOLDER_BACK}/{file_name}.png")
    front_gif = download_file(animated["front_default"], f"{settings.FOLDER_ANIM_FRONT}/{file_name}.gif")
    cry_path = download_file(data["cries"]["latest"], f"{settings.FOLDER_CRIES}/{file_name}.ogg")
    back_gif = download_file(animated["back_default"], f"{settings.FOLDER_ANIM_BACK}/{file_name}.gif")

    player_size = settings.PLAYER_SIZE_OVERRIDES.get(name, settings.PLAYER_SPRITE_SIZE)
    enemy_size = settings.ENEMY_SIZE_OVERRIDES.get(name, settings.ENEMY_SPRITE_SIZE)

    menu_image = load_sprite(front_png, settings.SELECT_SPRITE_SIZE)
    back_frames = load_frames(back_gif, back_png, player_size)
    front_frames = load_frames(front_gif, front_png, enemy_size)

    if back_frames is None:
        back_frames = flip_frames(load_frames(front_gif, front_png, player_size))

    stats = all_stats[name]
    types = []
    for item in data["types"]:
        types.append(item["type"]["name"])
    moves = all_moves.get(name, [])

    cry = sound.load_sound(cry_path, settings.CRY_VOLUME)

    return Pokemon(name, types, stats, moves, menu_image, back_frames, front_frames, cry)


def create_pokedex():
    all_stats = load_stats()
    all_moves = load_moves()
    pokedex = {}

    for name in settings.POKEMON_NAMES:
        pokemon = load_pokemon(name, all_stats, all_moves)
        if pokemon is not None:
            pokedex[name] = pokemon

    return pokedex


pokedex = create_pokedex()
