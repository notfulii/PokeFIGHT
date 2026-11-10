import pygame
import settings
import backgrounds
import auth
import ui
from input_box import InputBox


class LoginScreen:
    def __init__(self, player):
        self.player = player
        self.user = None
        self.blocked_user = None
        self.message = ""

        self.font = pygame.font.Font(settings.TEXT_FONT, settings.LOGIN_TEXT_SIZE)

        self.username_box = InputBox(settings.INPUT_X, settings.INPUT_USER_Y, self.font)
        self.password_box = InputBox(settings.INPUT_X, settings.INPUT_PASSWORD_Y, self.font, hidden=True)
        self.username_box.active = True

        login_x, login_y = settings.LOGIN_BUTTON_POSITION
        create_x, create_y = settings.CREATE_ACCOUNT_POSITION
        exit_x, exit_y = settings.LOGIN_EXIT_POSITION

        self.login_button = pygame.Rect(login_x, login_y, settings.LOGIN_BUTTON_WIDTH, settings.LOGIN_BUTTON_HEIGHT)
        self.create_button = pygame.Rect(create_x, create_y, settings.LOGIN_BUTTON_WIDTH, settings.LOGIN_BUTTON_HEIGHT)
        self.exit_button = pygame.Rect(exit_x, exit_y, settings.EXIT_WIDTH, settings.EXIT_HEIGHT)

    def is_player_one(self):
        return self.player == "one"

    def reset(self, blocked_user):
        self.user = None
        self.blocked_user = blocked_user
        self.message = ""
        self.username_box.text = ""
        self.password_box.text = ""
        self.username_box.active = True
        self.password_box.active = False

    def after_register(self, username):
        self.username_box.text = username
        self.password_box.text = ""
        self.message = settings.MESSAGE_ACCOUNT_CREATED
        self.username_box.active = False
        self.password_box.active = True

    def handle_event(self, event):
        self.username_box.handle_event(event)
        self.password_box.handle_event(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            self.switch_box()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return self.try_login()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.login_button.collidepoint(event.pos):
                return self.try_login()
            if self.create_button.collidepoint(event.pos):
                return "register"
            if self.exit_button.collidepoint(event.pos):
                if self.is_player_one():
                    return "quit"
                return "rankings"

        return None

    def switch_box(self):
        if self.username_box.active:
            self.username_box.active = False
            self.password_box.active = True
        else:
            self.username_box.active = True
            self.password_box.active = False

    def try_login(self):
        username = self.username_box.text.strip()
        password = self.password_box.text

        if username == "" or password == "":
            self.message = settings.MESSAGE_EMPTY_FIELDS
            return None

        if self.blocked_user is not None and username.lower() == self.blocked_user.lower():
            self.message = settings.MESSAGE_SAME_ACCOUNT
            return None

        if not auth.login(username, password):
            self.message = settings.MESSAGE_WRONG_LOGIN
            return None

        self.user = username
        if self.is_player_one():
            return "difficulty"
        return "rankings"

    def draw(self, screen):
        screen.blit(backgrounds.get_current(), (0, 0))

        if self.is_player_one():
            title = settings.LOGIN_TITLE
            exit_text = settings.EXIT_TEXT
        else:
            title = settings.LOGIN_TWO_TITLE
            exit_text = settings.BACK_TEXT

        ui.draw_centered_text(screen, self.font, title, settings.CENTER_X, settings.LOGIN_TITLE_Y)
        ui.draw_centered_text(screen, self.font, settings.LOGIN_USER_LABEL, settings.CENTER_X, settings.LOGIN_USER_LABEL_Y)
        ui.draw_centered_text(screen, self.font, settings.LOGIN_PASSWORD_LABEL, settings.CENTER_X, settings.LOGIN_PASSWORD_LABEL_Y)

        self.username_box.draw(screen)
        self.password_box.draw(screen)

        ui.draw_button(screen, self.font, self.login_button, settings.LOGIN_BUTTON_TEXT, settings.BUTTON_COLOR)
        ui.draw_button(screen, self.font, self.create_button, settings.CREATE_ACCOUNT_TEXT, settings.BUTTON_COLOR)
        ui.draw_button(screen, self.font, self.exit_button, exit_text, settings.BUTTON_COLOR)

        if self.message != "":
            ui.draw_centered_text(screen, self.font, self.message, settings.CENTER_X, settings.LOGIN_MESSAGE_Y)
