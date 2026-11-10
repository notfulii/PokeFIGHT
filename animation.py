import pygame
import settings
from PIL import Image, ImageSequence


def load_gif(path, max_size):
    gif = Image.open(path)
    frames = []

    for gif_frame in ImageSequence.Iterator(gif):
        rgba = gif_frame.convert("RGBA")
        image = pygame.image.frombytes(rgba.tobytes(), rgba.size, "RGBA")

        time = gif_frame.info.get("duration", settings.GIF_DEFAULT_FRAME_TIME)
        if time < settings.GIF_MIN_FRAME_TIME:
            time = settings.GIF_MIN_FRAME_TIME

        frames.append({"image": image, "time": time})

    visible_area = frames[0]["image"].get_bounding_rect()
    for frame in frames:
        visible_area.union_ip(frame["image"].get_bounding_rect())

    biggest_side = max(visible_area.width, visible_area.height)
    factor = max_size / biggest_side
    new_width = int(visible_area.width * factor)
    new_height = int(visible_area.height * factor)

    for frame in frames:
        cropped = frame["image"].subsurface(visible_area).copy()
        frame["image"] = pygame.transform.scale(cropped, (new_width, new_height)).convert_alpha()

    return frames


class AnimatedSprite:
    def __init__(self, frames):
        self.frames = frames
        self.index = 0
        self.last_change = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        frame_time = self.frames[self.index]["time"]

        if now - self.last_change >= frame_time:
            self.index = self.index + 1
            if self.index == len(self.frames):
                self.index = 0
            self.last_change = now

    def get_image(self):
        return self.frames[self.index]["image"]
