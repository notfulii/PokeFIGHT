import json
import os
import queue
import threading
import pygame
import settings
import get_pokemon

commands = queue.Queue()
saving = {"on": True}
console = {"open": False, "text": "", "lines": [], "font": None, "help_shown": False}

SCREEN_NAMES = ["start", "login", "register", "difficulty", "select", "battle", "result", "login_two", "rankings"]
MODES = ["easy", "hard", "multiplayer"]
SCREENS_THAT_NEED_A_MODE = ["select", "battle"]


def add_line(text):
    print(text)
    console["lines"].append(text)
    if len(console["lines"]) > settings.DEBUG_MAX_LINES:
        console["lines"].pop(0)


def say(text):
    add_line(f"DEBUG: {text}")


def read_commands():
    while True:
        try:
            commands.put(input())
        except EOFError:
            break


def start(screens):
    if not settings.DEBUG_ON:
        return None

    console["font"] = pygame.font.SysFont(settings.DEBUG_FONT, settings.DEBUG_TEXT_SIZE)
    threading.Thread(target=read_commands, daemon=True).start()
    say("console ready, press ` in the game or type 'help' here")

    if settings.DEBUG_RESUME:
        return load_saved(screens)
    return None


def is_console_key(event):
    if event.type != pygame.KEYDOWN:
        return False
    return pygame.key.name(event.key) in settings.DEBUG_KEYS


def handle_event(event):
    if not settings.DEBUG_ON:
        return False

    if is_console_key(event):
        console["open"] = not console["open"]
        console["text"] = ""
        if console["open"] and not console["help_shown"]:
            show_help()
            console["help_shown"] = True
        return True

    if not console["open"]:
        return False

    if event.type == pygame.TEXTINPUT:
        if event.text not in settings.DEBUG_KEYS:
            console["text"] = console["text"] + event.text
        return True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            add_line("> " + console["text"])
            commands.put(console["text"])
            console["text"] = ""
        elif event.key == pygame.K_BACKSPACE:
            console["text"] = console["text"][:-1]
        elif event.key == pygame.K_ESCAPE:
            console["open"] = False
        return True

    return False


def draw(screen):
    if not settings.DEBUG_ON or not console["open"]:
        return

    panel = pygame.Surface((settings.WINDOW_WIDTH, settings.DEBUG_PANEL_HEIGHT), pygame.SRCALPHA)
    panel.fill(settings.DEBUG_PANEL_COLOR)
    screen.blit(panel, (0, 0))

    font = console["font"]
    x = settings.DEBUG_MARGIN
    y = settings.DEBUG_MARGIN
    for line in console["lines"]:
        screen.blit(font.render(line, False, settings.DEBUG_TEXT_COLOR), (x, y))
        y = y + settings.DEBUG_LINE_GAP

    input_y = settings.DEBUG_PANEL_HEIGHT - settings.DEBUG_MARGIN - settings.DEBUG_LINE_GAP
    blink_number = pygame.time.get_ticks() // settings.BLINK_TIME
    if blink_number % 2 == 0:
        cursor = "_"
    else:
        cursor = ""
    screen.blit(font.render("> " + console["text"] + cursor, False, settings.DEBUG_INPUT_COLOR), (x, input_y))


def show_help():
    for line in settings.DEBUG_HELP:
        add_line("  " + line)


def find_pokemon(typed_name):
    for name in get_pokemon.pokedex:
        if name.lower() == typed_name.lower():
            return name
    return None


def set_mode(screens, mode):
    screens["difficulty"].mode = mode
    screens["select"].mode = mode


def prepare_mode(screens):
    if screens["difficulty"].mode is None:
        set_mode(screens, settings.DEBUG_DEFAULT_MODE)
        say(f"no mode chosen, using {settings.DEBUG_DEFAULT_MODE}")


def prepare_battle(screens):
    prepare_mode(screens)
    select = screens["select"]
    select.mode = screens["difficulty"].mode
    pokemon_names = list(get_pokemon.pokedex.keys())

    if select.player_one_choice is None:
        select.player_one_choice = pokemon_names[0]

    if select.mode == "multiplayer" and select.player_two_choice is None:
        for name in pokemon_names:
            if name != select.player_one_choice:
                select.player_two_choice = name
                break


def go_to(screens, screen_name):
    if screen_name not in SCREEN_NAMES:
        say("that screen does not exist, type 'screens' to see them")
        return None

    if screen_name in SCREENS_THAT_NEED_A_MODE:
        prepare_mode(screens)
    if screen_name == "battle":
        prepare_battle(screens)

    say(f"going to {screen_name}")
    return screen_name


def pick(screens, words):
    select = screens["select"]

    player_one = find_pokemon(words[1])
    if player_one is None:
        say(f"'{words[1]}' is not in POKEMON_NAMES")
        return
    select.player_one_choice = player_one

    if len(words) == 3:
        player_two = find_pokemon(words[2])
        if player_two is None:
            say(f"'{words[2]}' is not in POKEMON_NAMES")
            return
        if player_two == player_one:
            say("both players can not use the same pokemon")
            return
        select.player_two_choice = player_two

    say(f"picked {select.player_one_choice} and {select.player_two_choice}, type 'go battle' to fight")


def set_names(screens, words):
    screens["login"].user = words[1]
    say(f"player 1 is now {words[1]}")


def end_battle(battle, loser):
    loser.current_hp = 0
    battle.loser = loser
    battle.state = "over"


def hurt(battle, pokemon, amount):
    pokemon.take_damage(amount)
    say(f"{pokemon.name} {pokemon.current_hp}/{pokemon.max_hp}")
    if pokemon.is_fainted():
        end_battle(battle, pokemon)


def battle_command(screens, current_name, words):
    battle = screens["battle"]
    if current_name != "battle" or battle.player_one is None:
        say("this command only works inside a battle")
        return

    if words[0] == "heal":
        battle.player_one.heal()
        battle.player_two.heal()
        say("both healed")
    elif words[0] == "win":
        end_battle(battle, battle.player_two)
        say("you win")
    elif words[0] == "lose":
        end_battle(battle, battle.player_one)
        say("you lose")
    elif len(words) == 2 and words[1].isdigit() and words[0] == "enemy":
        hurt(battle, battle.player_two, int(words[1]))
    elif len(words) == 2 and words[1].isdigit() and words[0] == "player":
        hurt(battle, battle.player_one, int(words[1]))
    else:
        say("use: enemy <amount> | player <amount>")


def run_command(screens, current_name, words):
    command = words[0].lower()

    if command == "help":
        show_help()
    elif command == "screens":
        say("screens: " + ", ".join(SCREEN_NAMES))
    elif command == "where":
        say(f"you are in {current_name}, mode {screens['difficulty'].mode}")
    elif command == "go" and len(words) == 2:
        return go_to(screens, words[1].lower())
    elif command == "mode" and len(words) == 2 and words[1].lower() in MODES:
        set_mode(screens, words[1].lower())
        say(f"mode is now {words[1].lower()}")
    elif command == "pick" and (len(words) == 2 or len(words) == 3):
        pick(screens, words)
    elif command == "names" and len(words) == 2:
        set_names(screens, words)
    elif command in ["heal", "win", "lose", "enemy", "player"]:
        battle_command(screens, current_name, words)
    elif command == "forget":
        forget_saved()
    else:
        say("unknown command, type 'help'")

    return None


def run(screens, current_name):
    if not settings.DEBUG_ON:
        return None

    wanted_screen = None
    while not commands.empty():
        words = commands.get().split()
        if len(words) == 0:
            continue

        result = run_command(screens, current_name, words)
        if result is not None:
            wanted_screen = result

    return wanted_screen


def remember(screens, current_name):
    if not settings.DEBUG_ON or not settings.DEBUG_RESUME or not saving["on"]:
        return

    saved = {
        "screen": current_name,
        "mode": screens["difficulty"].mode,
        "player_one": screens["select"].player_one_choice,
        "player_two": screens["select"].player_two_choice,
        "name_one": screens["login"].user
    }

    with open(settings.DEBUG_FILE, "w", encoding="utf-8") as file:
        json.dump(saved, file, indent=4)


def load_saved(screens):
    if not os.path.exists(settings.DEBUG_FILE):
        return None

    with open(settings.DEBUG_FILE, "r", encoding="utf-8") as file:
        saved = json.load(file)

    if saved["screen"] not in SCREEN_NAMES or saved["screen"] == "start":
        return None

    if saved["mode"] in MODES:
        set_mode(screens, saved["mode"])
    if saved["player_one"] is not None:
        screens["select"].player_one_choice = find_pokemon(saved["player_one"])
    if saved["player_two"] is not None:
        screens["select"].player_two_choice = find_pokemon(saved["player_two"])
    screens["login"].user = saved.get("name_one")

    say(f"back to {saved['screen']} (type 'forget' to start from the beginning next time)")
    return go_to(screens, saved["screen"])


def forget_saved():
    saving["on"] = False
    if os.path.exists(settings.DEBUG_FILE):
        os.remove(settings.DEBUG_FILE)
    say("saved screen deleted, next time the game starts from the beginning")
