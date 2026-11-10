import pygame
import settings
import backgrounds
import ui


class DifficultyScreen:
    def __init__(self):
        self.mode = None

        self.font = pygame.font.Font(settings.TEXT_FONT, settings.MODE_TEXT_SIZE)

        x = settings.MODE_BUTTON_X
        width = settings.MODE_BUTTON_WIDTH
        height = settings.MODE_BUTTON_HEIGHT

        self.easy_button = pygame.Rect(x, settings.MODE_EASY_Y, width, height)
        self.hard_button = pygame.Rect(x, settings.MODE_HARD_Y, width, height)
        self.multiplayer_button = pygame.Rect(x, settings.MODE_MULTIPLAYER_Y, width, height)

    def handle_event(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return None

        if self.easy_button.collidepoint(event.pos):
            self.mode = "easy"
            return "select"
        if self.hard_button.collidepoint(event.pos):
            self.mode = "hard"
            return "select"
        if self.multiplayer_button.collidepoint(event.pos):
            self.mode = "multiplayer"
            return "select"

        return None

    def draw(self, screen):
        screen.blit(backgrounds.get_current(), (0, 0))
        ui.draw_centered_text(screen, self.font, settings.MODE_TITLE, settings.CENTER_X, settings.MODE_TITLE_Y)
        ui.draw_button(screen, self.font, self.easy_button, settings.EASY_TEXT, settings.EASY_COLOR)
        ui.draw_button(screen, self.font, self.hard_button, settings.HARD_TEXT, settings.HARD_COLOR)
        ui.draw_button(screen, self.font, self.multiplayer_button, settings.MULTIPLAYER_TEXT, settings.MULTIPLAYER_COLOR)
