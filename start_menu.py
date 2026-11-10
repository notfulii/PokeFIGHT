import pygame
import settings
import backgrounds
import ui


class StartScreen:
    def __init__(self):
        self.title = ui.load_image(settings.TITLE_IMAGE, settings.START_TITLE_WIDTH, settings.START_TITLE_HEIGHT)
        self.font = pygame.font.Font(settings.TEXT_FONT, settings.START_TEXT_SIZE)
        self.legal_font = pygame.font.Font(settings.TEXT_FONT, settings.LEGAL_TEXT_SIZE)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return "login"
        return None

    def draw(self, screen):
        screen.blit(backgrounds.get_current(), (0, 0))
        screen.blit(self.title, settings.START_TITLE_POSITION)

        blink_number = pygame.time.get_ticks() // settings.BLINK_TIME
        if blink_number % 2 == 0:
            ui.draw_centered_text(screen, self.font, settings.START_TEXT, settings.CENTER_X, settings.START_TEXT_Y)

        y = settings.LEGAL_FIRST_Y
        for line in settings.LEGAL_LINES:
            ui.draw_centered_text(screen, self.legal_font, line, settings.CENTER_X, y, settings.LEGAL_COLOR)
            y = y + settings.LEGAL_LINE_GAP
