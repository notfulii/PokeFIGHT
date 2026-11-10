import random
import pygame
import settings
import ui
import sound
from get_pokemon import pokedex
from animation import AnimatedSprite


class BattleScreen:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.mode = None

        self.player_one_name = settings.PLAYER_ONE_LABEL
        self.player_two_name = settings.PLAYER_TWO_LABEL

        self.attacker = None
        self.defender = None
        self.turn = 1

        self.player_one_animation = None
        self.player_two_animation = None

        self.state = "choose"
        self.message = ""
        self.loser = None

        self.current_move = None
        self.current_damage = 0
        self.current_effectiveness = 1
        self.current_critical = False
        self.damage_done = False
        self.attack_start = 0

        self.background = pygame.image.load(settings.BACKGROUND_FIGHT).convert()
        self.background = pygame.transform.scale(self.background, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

        self.dock = ui.load_image(settings.DOCK_IMAGE, settings.DOCK_SIZE, settings.DOCK_SIZE)
        self.over_dock = ui.load_image(settings.OVER_DOCK_IMAGE, settings.DOCK_SIZE, settings.DOCK_SIZE)

        self.font = pygame.font.Font(settings.TEXT_FONT, settings.BATTLE_TEXT_SIZE)
        self.turn_font = pygame.font.Font(settings.TEXT_FONT, settings.TURN_TEXT_SIZE)

        self.panel = pygame.Surface((settings.PANEL_WIDTH, settings.PANEL_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.panel, settings.PANEL_COLOR, self.panel.get_rect(), border_radius=settings.PANEL_RADIUS)

        self.move_buttons = []
        for position in settings.MOVE_BUTTON_POSITIONS:
            x, y = position
            rect = pygame.Rect(x, y, settings.MOVE_BUTTON_WIDTH, settings.MOVE_BUTTON_HEIGHT)
            self.move_buttons.append(rect)

    def start(self, player_one_name, player_two_name, mode):
        if player_two_name is None:
            options = []
            for name in pokedex:
                if name != player_one_name:
                    options.append(name)
            player_two_name = random.choice(options)

        self.setup(player_one_name, player_two_name, mode)

    def setup(self, player_one_name, player_two_name, mode):
        self.player_one = pokedex[player_one_name]
        self.player_two = pokedex[player_two_name]
        self.mode = mode

        self.player_one.set_battle_hp(self.get_hp_multiplier(self.player_one))
        self.player_two.set_battle_hp(self.get_hp_multiplier(self.player_two))

        self.player_one_animation = AnimatedSprite(self.player_one.back_frames)
        self.player_two_animation = AnimatedSprite(self.player_two.front_frames)

        self.message = ""
        self.loser = None
        self.turn = 1

        if self.player_one.speed >= self.player_two.speed:
            self.attacker = self.player_one
            self.defender = self.player_two
        else:
            self.attacker = self.player_two
            self.defender = self.player_one

        self.start_turn()

    def get_hp_multiplier(self, pokemon):
        if self.mode == "multiplayer":
            return settings.MULTIPLAYER_HP

        if self.mode == "hard":
            if pokemon is self.player_one:
                return settings.HARD_PLAYER_HP
            return settings.HARD_CPU_HP

        if pokemon is self.player_one:
            return settings.EASY_PLAYER_HP
        return settings.EASY_CPU_HP

    def is_cpu_turn(self):
        return self.mode != "multiplayer" and self.attacker is self.player_two

    def start_turn(self):
        if self.is_cpu_turn():
            self.attack(self.choose_cpu_move())
        else:
            self.state = "choose"

    def choose_cpu_move(self):
        if self.mode != "hard":
            return random.choice(self.attacker.moves)

        best_move = self.attacker.moves[0]
        best_damage = 0
        for move in self.attacker.moves:
            damage = self.attacker.calculate_damage(self.defender, move)
            if damage > best_damage:
                best_damage = damage
                best_move = move
        return best_move

    def get_damage(self, move):
        damage = self.attacker.calculate_damage(self.defender, move)
        if damage == 0:
            return 0

        if self.current_critical:
            damage = int(damage * settings.CRIT_MULTIPLIER)

        if self.is_cpu_turn():
            if self.mode == "hard":
                damage = int(damage * settings.HARD_CPU_DAMAGE)
            else:
                damage = int(damage * settings.EASY_CPU_DAMAGE)

        if self.mode == "multiplayer":
            max_hit = int(self.defender.max_hp * settings.MULTIPLAYER_MAX_HIT)
        else:
            max_hit = int(self.defender.max_hp * settings.SINGLE_PLAYER_MAX_HIT)
        if damage > max_hit:
            damage = max_hit

        if damage < settings.MIN_DAMAGE:
            damage = settings.MIN_DAMAGE
        return damage

    def get_effect_text(self):
        texts = []
        if self.current_critical and self.current_effectiveness > 0:
            texts.append(settings.CRIT_TEXT)

        if self.current_effectiveness == 0:
            texts.append(settings.NO_EFFECT_TEXT)
        elif self.current_effectiveness > 1:
            texts.append(settings.SUPER_EFFECTIVE_TEXT)
        elif self.current_effectiveness < 1:
            texts.append(settings.NOT_EFFECTIVE_TEXT)

        return " ".join(texts)

    def attack(self, move):
        self.current_move = move
        self.current_effectiveness = self.attacker.get_effectiveness(move, self.defender)
        self.current_critical = random.random() < settings.CRIT_CHANCE
        self.current_damage = self.get_damage(move)
        self.damage_done = False
        self.attack_start = pygame.time.get_ticks()

        self.message = f"{self.attacker.name} used {self.get_move_title(move)}!"
        self.state = "animating"
        sound.play_sound(self.attacker.cry)

    def update_attack(self):
        time_passed = pygame.time.get_ticks() - self.attack_start

        if not self.damage_done and time_passed >= settings.LUNGE_TIME:
            self.defender.take_damage(self.current_damage)
            self.damage_done = True

        if time_passed >= settings.ATTACK_TOTAL_TIME:
            self.finish_attack()

    def finish_attack(self):
        self.message = f"{self.attacker.name} used {self.get_move_title(self.current_move)}! {self.current_damage} damage. {self.get_effect_text()}".strip()
        self.state = "message"

        if self.defender.is_fainted():
            self.loser = self.defender

    def next_turn(self):
        old_attacker = self.attacker
        self.attacker = self.defender
        self.defender = old_attacker
        self.turn = self.turn + 1
        self.start_turn()

    def continue_battle(self):
        if self.state == "fainted":
            self.state = "over"
        elif self.loser is not None:
            self.message = f"{self.loser.name} fainted!"
            self.state = "fainted"
            sound.play_sound(self.loser.cry)
        else:
            self.next_turn()

    def is_over(self):
        if self.player_one is None:
            return False
        if self.state == "over":
            return True
        if self.state == "choose":
            if self.player_one.is_fainted() or self.player_two.is_fainted():
                return True
        return False

    def get_winner(self):
        if self.player_two.is_fainted():
            return self.player_one
        return self.player_two

    def set_names(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name

    def get_winner_owner_name(self):
        if self.get_winner() is self.player_one:
            return self.player_one_name
        return self.player_two_name

    def human_won(self):
        if self.mode == "multiplayer":
            return True
        return self.get_winner() is self.player_one

    def get_result_title(self):
        if self.mode == "multiplayer":
            return f"{self.get_winner_owner_name().upper()} {settings.WINS_TEXT}"

        if self.get_winner() is self.player_one:
            return settings.WIN_TEXT
        return settings.LOSE_TEXT

    def get_result_color(self):
        if self.mode != "multiplayer" and self.get_winner() is self.player_two:
            return settings.LOSE_COLOR
        return settings.WIN_COLOR

    def get_owner_label(self, pokemon):
        if pokemon is self.player_one:
            return self.player_one_name
        return self.player_two_name

    def get_move_title(self, move):
        return move["name"].replace("-", " ").title()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return "select"
        if self.player_one is None:
            return None

        if self.state == "choose":
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click_move_button(event.pos)
        elif self.state == "message" or self.state == "fainted":
            clicked = event.type == pygame.MOUSEBUTTONDOWN
            pressed_enter = event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN
            if clicked or pressed_enter:
                self.continue_battle()

        return None

    def click_move_button(self, mouse_position):
        for number in range(len(self.attacker.moves)):
            if self.move_buttons[number].collidepoint(mouse_position):
                self.attack(self.attacker.moves[number])
                return

    def get_health_color(self, percent):
        if percent > settings.HEALTH_YELLOW_BELOW:
            return settings.HEALTH_GREEN
        if percent > settings.HEALTH_RED_BELOW:
            return settings.HEALTH_YELLOW
        return settings.HEALTH_RED

    def update_shown_hp(self, pokemon):
        if pokemon.shown_hp > pokemon.current_hp:
            pokemon.shown_hp = pokemon.shown_hp - settings.HP_DRAIN_PER_FRAME
            if pokemon.shown_hp < pokemon.current_hp:
                pokemon.shown_hp = pokemon.current_hp

        if pokemon.shown_hp < pokemon.current_hp:
            pokemon.shown_hp = pokemon.current_hp

    def draw_health_bar(self, screen, pokemon, bar):
        self.update_shown_hp(pokemon)

        x, y, full_width, height = bar
        percent = pokemon.shown_hp / pokemon.max_hp
        width = int(full_width * percent)

        pygame.draw.rect(screen, self.get_health_color(percent), (x, y, width, height))

    def draw_dock(self, screen, pokemon, dock_position, health_bar, name_position):
        screen.blit(self.dock, dock_position)
        self.draw_health_bar(screen, pokemon, health_bar)
        screen.blit(self.over_dock, dock_position)

        name_x, name_y = name_position
        ui.draw_centered_text(screen, self.font, pokemon.name, name_x, name_y)

    def get_feet(self, pokemon):
        if pokemon is self.player_one:
            return settings.PLAYER_FEET
        return settings.ENEMY_FEET

    def get_lunge_offset(self, pokemon):
        if self.state != "animating" or pokemon is not self.attacker:
            return 0, 0

        time_passed = pygame.time.get_ticks() - self.attack_start
        if time_passed < settings.LUNGE_TIME:
            progress = time_passed / settings.LUNGE_TIME
        elif time_passed < settings.LUNGE_TIME + settings.RETURN_TIME:
            progress = 1 - (time_passed - settings.LUNGE_TIME) / settings.RETURN_TIME
        else:
            progress = 0

        my_x, my_y = self.get_feet(self.attacker)
        target_x, target_y = self.get_feet(self.defender)
        offset_x = (target_x - my_x) * settings.LUNGE_PERCENT * progress
        offset_y = (target_y - my_y) * settings.LUNGE_PERCENT * progress
        return int(offset_x), int(offset_y)

    def is_being_hit(self, pokemon):
        if self.state != "animating" or pokemon is not self.defender:
            return False
        if not self.damage_done:
            return False

        time_passed = pygame.time.get_ticks() - self.attack_start
        return time_passed < settings.LUNGE_TIME + settings.HIT_TIME

    def get_shake_offset(self, pokemon):
        if not self.is_being_hit(pokemon):
            return 0

        shake_number = pygame.time.get_ticks() // settings.SHAKE_SPEED
        if shake_number % 2 == 0:
            return settings.SHAKE_DISTANCE
        return -settings.SHAKE_DISTANCE

    def make_red(self, image):
        red_image = image.copy()
        red_image.fill(settings.HIT_RED, special_flags=pygame.BLEND_RGB_ADD)
        return red_image

    def draw_pokemon(self, screen, pokemon, animation):
        animation.update()
        image = animation.get_image()

        if self.is_being_hit(pokemon):
            flash_number = pygame.time.get_ticks() // settings.FLASH_SPEED
            if flash_number % 2 == 0:
                image = self.make_red(image)

        lunge_x, lunge_y = self.get_lunge_offset(pokemon)
        shake_x = self.get_shake_offset(pokemon)

        feet_x, feet_y = self.get_feet(pokemon)
        image_x = feet_x - image.get_width() // 2 + lunge_x + shake_x
        image_y = feet_y - image.get_height() + lunge_y
        screen.blit(image, (image_x, image_y))

    def draw_turn(self, screen):
        owner = self.get_owner_label(self.attacker)
        turn_text = f"Turn {self.turn} - {owner} ({self.attacker.name})"
        ui.draw_centered_text(screen, self.turn_font, turn_text, settings.CENTER_X, settings.TURN_TEXT_Y, settings.TURN_TEXT_COLOR)

        mode_text = settings.MODE_NAMES.get(self.mode, "")
        ui.draw_centered_text(screen, self.font, mode_text, settings.CENTER_X, settings.MODE_LABEL_Y)

    def draw_panel(self, screen):
        screen.blit(self.panel, settings.PANEL_POSITION)

        if self.state == "choose":
            for number in range(len(self.attacker.moves)):
                move = self.attacker.moves[number]
                color = settings.TYPE_COLORS.get(move["type"], settings.BUTTON_COLOR)
                ui.draw_button(screen, self.font, self.move_buttons[number], self.get_move_title(move), color)
        else:
            message_x, message_y = settings.MESSAGE_POSITION
            ui.draw_text(screen, self.font, self.message, message_x, message_y)

    def draw(self, screen):
        if self.state == "animating":
            self.update_attack()

        screen.blit(self.background, (0, 0))

        if self.attacker is self.player_one:
            self.draw_pokemon(screen, self.player_two, self.player_two_animation)
            self.draw_pokemon(screen, self.player_one, self.player_one_animation)
        else:
            self.draw_pokemon(screen, self.player_one, self.player_one_animation)
            self.draw_pokemon(screen, self.player_two, self.player_two_animation)

        self.draw_dock(screen, self.player_one, settings.PLAYER_DOCK_POSITION, settings.PLAYER_HEALTH_BAR, settings.PLAYER_NAME_POSITION)
        self.draw_dock(screen, self.player_two, settings.ENEMY_DOCK_POSITION, settings.ENEMY_HEALTH_BAR, settings.ENEMY_NAME_POSITION)

        self.draw_turn(screen)
        self.draw_panel(screen)
