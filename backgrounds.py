import os
import random
import pygame
import settings

loaded = {"images": {}, "current": None}


def fit_to_window(image):
    width_factor = settings.WINDOW_WIDTH / image.get_width()
    height_factor = settings.WINDOW_HEIGHT / image.get_height()
    factor = max(width_factor, height_factor)

    new_width = int(image.get_width() * factor) + 1
    new_height = int(image.get_height() * factor) + 1
    image = pygame.transform.smoothscale(image, (new_width, new_height))

    crop = pygame.Rect(0, 0, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
    crop.center = image.get_rect().center
    return image.subsurface(crop).copy()


def load_backgrounds():
    for file_name in os.listdir(settings.FOLDER_BACKGROUNDS):
        if file_name == settings.BATTLE_BACKGROUND:
            continue

        path = os.path.join(settings.FOLDER_BACKGROUNDS, file_name)
        image = pygame.image.load(path).convert()
        loaded["images"][file_name] = fit_to_window(image)

    loaded["current"] = settings.FIRST_BACKGROUND


def pick_new():
    options = []
    for file_name in loaded["images"]:
        if file_name != loaded["current"]:
            options.append(file_name)

    if len(options) > 0:
        loaded["current"] = random.choice(options)


def get_current():
    return loaded["images"][loaded["current"]]
