import pygame
import settings
import backgrounds
import auth
import ui
from input_box import InputBox


class RegisterScreen:
    def __init__(self):
        self.return_to = "login"
        self.created_user = None
        self.message = ""

        self.font = pygame.font.Font(settings.TEXT_FONT, settings.LOGIN_TEXT_SIZE)

        self.username_box = InputBox(settings.INPUT_X, settings.REGISTER_USER_Y, self.font)
        self.password_box = InputBox(settings.INPUT_X, settings.REGISTER_PASSWORD_Y, self.font, hidden=True)
        self.confirm_box = InputBox(settings.INPUT_X, settings.REGISTER_CONFIRM_Y, self.font, hidden=True)
        self.boxes = [self.username_box, self.password_box, self.confirm_box]
        self.username_box.active = True

        register_x, register_y = settings.REGISTER_BUTTON_POSITION
        back_x, back_y = settings.REGISTER_BACK_POSITION
        self.register_button = pygame.Rect(register_x, register_y, settings.LOGIN_BUTTON_WIDTH, settings.LOGIN_BUTTON_HEIGHT)
        self.back_button = pygame.Rect(back_x, back_y, settings.LOGIN_BUTTON_WIDTH, settings.LOGIN_BUTTON_HEIGHT)

    def reset(self, return_to):
        self.return_to = return_to
        self.created_user = None
        self.message = ""
        for box in self.boxes:
            box.text = ""
            box.active = False
        self.username_box.active = True

    def switch_box(self):
        for number in range(len(self.boxes)):
            if self.boxes[number].active:
                self.boxes[number].active = False
                next_number = (number + 1) % len(self.boxes)
                self.boxes[next_number].active = True
                return
        self.username_box.active = True

    def try_register(self):
        username = self.username_box.text.strip()
        password = self.password_box.text
        confirm = self.confirm_box.text

        if self.username_box.text == "" or password == "":
            self.message = settings.MESSAGE_EMPTY_FIELDS
        elif username == "" or password.strip() == "":
            self.message = settings.MESSAGE_ONLY_SPACES
        elif len(password) < settings.PASSWORD_MIN_LENGTH:
            self.message = settings.MESSAGE_SHORT_PASSWORD
        elif password != confirm:
            self.message = settings.MESSAGE_PASSWORDS_DIFFERENT
        elif auth.register(username, password):
            self.created_user = username
            return self.return_to
        else:
            self.message = settings.MESSAGE_USER_EXISTS
        return None

    def handle_event(self, event):
        for box in self.boxes:
            box.handle_event(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            self.switch_box()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return self.try_register()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.register_button.collidepoint(event.pos):
                return self.try_register()
            if self.back_button.collidepoint(event.pos):
                return self.return_to

        return None

    def draw(self, screen):
        screen.blit(backgrounds.get_current(), (0, 0))

        ui.draw_centered_text(screen, self.font, settings.REGISTER_TITLE, settings.CENTER_X, settings.REGISTER_TITLE_Y)
        ui.draw_centered_text(screen, self.font, settings.LOGIN_USER_LABEL, settings.CENTER_X, settings.REGISTER_USER_LABEL_Y)
        ui.draw_centered_text(screen, self.font, settings.LOGIN_PASSWORD_LABEL, settings.CENTER_X, settings.REGISTER_PASSWORD_LABEL_Y)
        ui.draw_centered_text(screen, self.font, settings.REGISTER_CONFIRM_LABEL, settings.CENTER_X, settings.REGISTER_CONFIRM_LABEL_Y)

        for box in self.boxes:
            box.draw(screen)

        ui.draw_button(screen, self.font, self.register_button, settings.REGISTER_BUTTON_TEXT, settings.REGISTER_BUTTON_COLOR)
        ui.draw_button(screen, self.font, self.back_button, settings.BACK_TEXT, settings.BUTTON_COLOR)

        if self.message != "":
            ui.draw_centered_text(screen, self.font, self.message, settings.CENTER_X, settings.REGISTER_MESSAGE_Y)
