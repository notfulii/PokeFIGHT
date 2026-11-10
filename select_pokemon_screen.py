import pygame
import settings
import backgrounds
import ui
import sound
from get_pokemon import pokedex


class SelectScreen:
    def __init__(self):
        self.mode = None
        self.player_one_choice = None
        self.player_two_choice = None
        self.picking = "one"

        self.title = ui.load_image(settings.TITLE_IMAGE, settings.SELECT_TITLE_WIDTH, settings.SELECT_TITLE_HEIGHT)

        self.font = pygame.font.Font(settings.TEXT_FONT, settings.SELECT_TEXT_SIZE)
        self.exit_font = pygame.font.Font(settings.TEXT_FONT, settings.EXIT_TEXT_SIZE)
        self.change_mode_font = pygame.font.Font(settings.TEXT_FONT, settings.CHANGE_TEXT_SIZE)
        self.play_font = pygame.font.Font(settings.TEXT_FONT, settings.PLAY_TEXT_SIZE)
        self.trophy = ui.load_icon(settings.RANKING_IMAGE, settings.RANK_ICON_SIZE)

        play_x, play_y = settings.PLAY_BUTTON_POSITION
        self.play_button = pygame.Rect(play_x, play_y, settings.PLAY_WIDTH, settings.PLAY_HEIGHT)

        exit_x, exit_y = settings.SELECT_EXIT_POSITION
        self.exit_button = pygame.Rect(exit_x, exit_y, settings.EXIT_WIDTH, settings.EXIT_HEIGHT)
        
        change_button_x, change_button_y = settings.CHANGE_BUTTON_POSITION
        self.change_mode_button = pygame.Rect(change_button_x, change_button_y, settings.CHANGE_WIDTH, settings.CHANGE_HEIGHT)
        
        rank_button_x, rank_button_y = settings.RANK_BUTTON_POSITION
        self.rank_button = pygame.Rect(rank_button_x, rank_button_y, settings.RANK_WIDTH, settings.RANK_HEIGHT)

        self.box_image = pygame.Surface((settings.BOX_SIZE, settings.BOX_SIZE), pygame.SRCALPHA)
        box_area = self.box_image.get_rect()
        pygame.draw.rect(self.box_image, settings.BOX_COLOR, box_area, border_radius=settings.BOX_RADIUS)
        pygame.draw.rect(self.box_image, settings.BOX_BORDER_COLOR, box_area, settings.BOX_BORDER_WIDTH, border_radius=settings.BOX_RADIUS)

        self.boxes = self.create_boxes()

    def create_boxes(self):
        names = list(pokedex.keys())
        boxes = []
        index = 0

        for row in range(settings.ROWS):
            for column in range(settings.COLUMNS):
                if index == len(names):
                    return boxes

                x = settings.GRID_X + column * settings.CELL_SIZE
                y = settings.GRID_Y + row * settings.CELL_SIZE
                rect = pygame.Rect(x, y, settings.BOX_SIZE, settings.BOX_SIZE)

                boxes.append({"name": names[index], "rect": rect})
                index = index + 1

        return boxes

    def reset(self, mode):
        self.mode = mode
        self.player_one_choice = None
        self.player_two_choice = None
        self.picking = "one"

    def choose(self, name):
        if self.mode != "multiplayer":
            self.player_one_choice = name
            sound.play_sound(pokedex[name].cry)
            return

        if self.picking == "one":
            if name == self.player_two_choice:
                return
            self.player_one_choice = name
            self.picking = "two"
        else:
            if name == self.player_one_choice:
                return
            self.player_two_choice = name
            self.picking = "one"

        sound.play_sound(pokedex[name].cry)

    def is_ready(self):
        if self.player_one_choice is None:
            return False
        if self.mode == "multiplayer" and self.player_two_choice is None:
            return False
        return True

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if self.is_ready():
                return "battle"

        if event.type != pygame.MOUSEBUTTONDOWN:
            return None

        if self.exit_button.collidepoint(event.pos):
            return "quit"

        if self.change_mode_button.collidepoint(event.pos):
            return "difficulty"
        
        if self.rank_button.collidepoint(event.pos):
            return "rankings"

        if self.play_button.collidepoint(event.pos):
            if self.is_ready():
                return "battle"
            return None

        for box in self.boxes:
            if box["rect"].collidepoint(event.pos):
                self.choose(box["name"])

        return None

    def get_header_text(self):
        if self.is_ready():
            return settings.SELECT_READY_TEXT
        if self.mode != "multiplayer":
            return settings.SELECT_TEXT
        if self.picking == "one":
            return settings.SELECT_PLAYER_ONE_TEXT
        return settings.SELECT_PLAYER_TWO_TEXT

    def get_picking_color(self):
        if self.picking == "one":
            return settings.PLAYER_ONE_COLOR
        return settings.PLAYER_TWO_COLOR

    def get_bounce(self):
        bounce_number = pygame.time.get_ticks() // settings.PERSON_BOUNCE_SPEED
        if bounce_number % 2 == 0:
            return settings.PERSON_BOUNCE
        return 0

    def draw_player_mark(self, screen, rect, color, offset):
        pygame.draw.rect(screen, color, rect, settings.BOX_BORDER_WIDTH, border_radius=settings.BOX_RADIUS)

        offset_x, offset_y = offset
        person_x = rect.x + offset_x
        person_y = rect.y + offset_y - self.get_bounce()
        ui.draw_person(screen, color, person_x, person_y)

    def draw(self, screen):
        screen.blit(backgrounds.get_current(), (0, 0))
        screen.blit(self.title, settings.SELECT_TITLE_POSITION)

        text_x, text_y = settings.SELECT_TEXT_POSITION
        ui.draw_text(screen, self.font, self.get_header_text(), text_x, text_y)

        ui.draw_button(screen, self.exit_font, self.exit_button, settings.EXIT_TEXT, settings.BUTTON_COLOR)
        ui.draw_button(screen, self.change_mode_font, self.change_mode_button, settings.CHANGE_MODE_BUTTON_TEXT, settings.CHANGE_BUTTON_COLOR)
        ui.draw_icon_button(screen, self.rank_button, self.trophy, settings.RANK_BUTTON_COLOR)

        if self.is_ready():
            play_color = settings.PLAY_COLOR
        else:
            play_color = settings.PLAY_DISABLED_COLOR
        ui.draw_button(screen, self.play_font, self.play_button, settings.PLAY_TEXT, play_color)

        mouse_position = pygame.mouse.get_pos()

        for box in self.boxes:
            rect = box["rect"]
            image = pokedex[box["name"]].menu_image
            image_x = rect.centerx - image.get_width() // 2
            image_y = rect.centery - image.get_height() // 2

            screen.blit(self.box_image, rect)
            screen.blit(image, (image_x, image_y))

            if rect.collidepoint(mouse_position):
                pygame.draw.rect(screen, self.get_picking_color(), rect, settings.BOX_BORDER_WIDTH, border_radius=settings.BOX_RADIUS)

            if box["name"] == self.player_one_choice:
                self.draw_player_mark(screen, rect, settings.PLAYER_ONE_COLOR, settings.PERSON_ONE_OFFSET)

            if box["name"] == self.player_two_choice:
                self.draw_player_mark(screen, rect, settings.PLAYER_TWO_COLOR, settings.PERSON_TWO_OFFSET)
