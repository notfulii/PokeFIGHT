import pygame
import settings


class Transition:
    def __init__(self):
        self.phase = None
        self.start_time = 0
        self.next_screen = None

        self.black_screen = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.black_screen.fill(settings.TRANSITION_COLOR)

    def start(self, next_screen):
        self.phase = "fade_out"
        self.start_time = pygame.time.get_ticks()
        self.next_screen = next_screen

    def is_active(self):
        return self.phase is not None

    def get_progress(self):
        time_passed = pygame.time.get_ticks() - self.start_time
        progress = time_passed / settings.TRANSITION_TIME
        if progress > 1:
            progress = 1
        return progress

    def update(self):
        if self.phase is None:
            return None
        if self.get_progress() < 1:
            return None

        if self.phase == "fade_out":
            self.phase = "fade_in"
            self.start_time = pygame.time.get_ticks()
            return self.next_screen

        self.phase = None
        return None

    def draw(self, screen):
        if self.phase is None:
            return

        progress = self.get_progress()
        if self.phase == "fade_out":
            darkness = progress * 255
        else:
            darkness = (1 - progress) * 255

        self.black_screen.set_alpha(int(darkness))
        screen.blit(self.black_screen, (0, 0))
