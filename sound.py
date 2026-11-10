import os
import pygame
import settings

playing = {"path": None}


def sound_works():
    return settings.SOUND_ON and pygame.mixer.get_init() is not None


def load_sound(path, volume):
    if path is None or not sound_works():
        return None

    sound = pygame.mixer.Sound(path)
    sound.set_volume(volume)
    return sound


def play_sound(sound):
    if sound is not None and sound_works():
        sound.play()


def play_music(path):
    if path == playing["path"]:
        return
    playing["path"] = path

    if not sound_works():
        return

    if path is None or not os.path.exists(path):
        pygame.mixer.music.stop()
        return

    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(settings.MUSIC_VOLUME)
    pygame.mixer.music.play(-1)
