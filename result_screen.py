import pygame
import settings
import backgrounds
import ui


class ResultScreen:
    def __init__(self):
        self.title = ""
        self.color = settings.WIN_COLOR
        self.winner = ""
        self.time_text = ""
        self.next_screen = "rankings"

        self.title_font = pygame.font.Font(settings.TEXT_FONT, settings.RESULT_TITLE_SIZE)
        self.font = pygame.font.Font(settings.TEXT_FONT, settings.RESULT_TEXT_SIZE)

    def show(self, title, color, winner, time_text, next_screen="rankings"):
        self.title = title
        self.color = color
        self.winner = winner
        self.time_text = time_text
        self.next_screen = next_screen

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return self.next_screen
        return None

    def draw(self, screen):
        screen.blit(backgrounds.get_current(), (0, 0))

        ui.draw_centered_text(screen, self.title_font, self.title, settings.CENTER_X, settings.RESULT_TITLE_Y, self.color)
        ui.draw_centered_text(screen, self.font, f"{self.winner} wins the battle", settings.CENTER_X, settings.RESULT_WINNER_Y)
        ui.draw_centered_text(screen, self.font, f"Time: {self.time_text}", settings.CENTER_X, settings.RESULT_TIME_Y, settings.RESULT_TIME_COLOR)

        blink_number = pygame.time.get_ticks() // settings.BLINK_TIME
        if blink_number % 2 == 0:
            ui.draw_centered_text(screen, self.font, settings.RESULT_TEXT, settings.CENTER_X, settings.RESULT_TEXT_Y)
