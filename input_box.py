import pygame
import settings


class InputBox:
    def __init__(self, x, y, font, hidden=False):
        self.rect = pygame.Rect(x, y, settings.INPUT_WIDTH, settings.INPUT_HEIGHT)
        self.font = font
        self.hidden = hidden
        self.text = ""
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if not self.active:
            return

        if event.type == pygame.TEXTINPUT:
            if len(self.text) < settings.INPUT_MAX_LENGTH:
                self.text = self.text + event.text

        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]

    def draw(self, screen):
        if self.active:
            border_color = settings.INPUT_ACTIVE_COLOR
        else:
            border_color = settings.INPUT_COLOR

        pygame.draw.rect(screen, settings.INPUT_BACKGROUND_COLOR, self.rect, border_radius=settings.INPUT_RADIUS)
        pygame.draw.rect(screen, border_color, self.rect, settings.INPUT_BORDER_WIDTH, border_radius=settings.INPUT_RADIUS)

        if self.hidden:
            shown_text = settings.PASSWORD_CHARACTER * len(self.text)
        else:
            shown_text = self.text

        text_image = self.font.render(shown_text, False, settings.INPUT_TEXT_COLOR)
        text_x = self.rect.x + settings.INPUT_TEXT_PADDING
        text_y = self.rect.centery - text_image.get_height() // 2
        screen.blit(text_image, (text_x, text_y))
