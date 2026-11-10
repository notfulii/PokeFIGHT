import pygame
import settings
import backgrounds
import ui
import rankings


class RankingsScreen:
    def __init__(self):
        self.records = []
        self.new_record = None

        self.title_font = pygame.font.Font(settings.TEXT_FONT, settings.RANKING_TITLE_SIZE)
        self.font = pygame.font.Font(settings.TEXT_FONT, settings.RANKING_TEXT_SIZE)

        self.panel = pygame.Surface((settings.RANKING_PANEL_WIDTH, settings.RANKING_PANEL_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.panel, settings.RANKING_PANEL_COLOR, self.panel.get_rect(), border_radius=settings.RANKING_PANEL_RADIUS)

    def show(self, new_record):
        self.new_record = new_record
        self.records = rankings.load_rankings()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return "select"
        return None

    def draw_row(self, screen, texts, y, color):
        for number in range(len(texts)):
            x = settings.RANKING_COLUMNS_X[number]
            ui.draw_text(screen, self.font, texts[number], x, y, color)

    def draw(self, screen):
        screen.blit(backgrounds.get_current(), (0, 0))
        screen.blit(self.panel, settings.RANKING_PANEL_POSITION)

        ui.draw_centered_text(screen, self.title_font, settings.RANKING_TITLE, settings.CENTER_X, settings.RANKING_TITLE_Y)
        self.draw_row(screen, settings.RANKING_HEADERS, settings.RANKING_HEADER_Y, settings.RANKING_HEADER_COLOR)

        if len(self.records) == 0:
            ui.draw_centered_text(screen, self.font, settings.RANKING_EMPTY_TEXT, settings.CENTER_X, settings.RANKING_FIRST_ROW_Y)

        y = settings.RANKING_FIRST_ROW_Y
        position = 1
        for record in self.records:
            if record == self.new_record:
                color = settings.RANKING_NEW_COLOR
            else:
                color = settings.TEXT_COLOR

            texts = [str(position), record["name"], record["pokemon"], record["mode"], rankings.format_time(record["time"])]
            self.draw_row(screen, texts, y, color)

            y = y + settings.RANKING_ROW_GAP
            position = position + 1

        blink_number = pygame.time.get_ticks() // settings.BLINK_TIME
        if blink_number % 2 == 0:
            ui.draw_centered_text(screen, self.font, settings.RESULT_TEXT, settings.CENTER_X, settings.RANKING_CONTINUE_Y)
