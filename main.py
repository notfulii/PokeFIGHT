import importlib
import pygame
import settings
import time

pygame.init()
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption(settings.GAME_TITLE)

if settings.START_FULLSCREEN:
    pygame.display.toggle_fullscreen()

import sound
import backgrounds
import ui
import pokeapi
import stats
import moves
import pokemon
import animation
import get_pokemon
import transition
import start_menu
import login_screen
import difficulty_screen
import select_pokemon_screen
import battle_screen
import result_screen
import register_screen
import rankings
import rankings_screen
import debug_console

modules_to_reload = [settings, ui, pokeapi, stats, moves, pokemon, animation, get_pokemon, transition, rankings,
                     start_menu, login_screen, register_screen, difficulty_screen, select_pokemon_screen,
                     battle_screen, result_screen, rankings_screen]


def create_screens():
    screens = {}
    screens["start"] = start_menu.StartScreen()
    screens["login"] = login_screen.LoginScreen("one")
    screens["login_two"] = login_screen.LoginScreen("two")
    screens["register"] = register_screen.RegisterScreen()
    screens["difficulty"] = difficulty_screen.DifficultyScreen()
    screens["select"] = select_pokemon_screen.SelectScreen()
    screens["battle"] = battle_screen.BattleScreen()
    screens["result"] = result_screen.ResultScreen()
    screens["rankings"] = rankings_screen.RankingsScreen()
    return screens


def reload_game(old_screens):
    old_login = old_screens["login"]
    old_login_two = old_screens["login_two"]
    old_select = old_screens["select"]
    old_battle = old_screens["battle"]
    old_result = old_screens["result"]
    old_rankings = old_screens["rankings"]

    for module in modules_to_reload:
        importlib.reload(module)

    new_screens = create_screens()

    new_screens["login"].username_box.text = old_login.username_box.text
    new_screens["login"].password_box.text = old_login.password_box.text
    new_screens["login"].user = old_login.user
    new_screens["login_two"].username_box.text = old_login_two.username_box.text
    new_screens["login_two"].blocked_user = old_login_two.blocked_user
    new_screens["difficulty"].mode = old_screens["difficulty"].mode
    new_screens["select"].mode = old_select.mode
    new_screens["select"].player_one_choice = old_select.player_one_choice
    new_screens["select"].player_two_choice = old_select.player_two_choice
    new_screens["result"].show(old_result.title, old_result.color, old_result.winner, old_result.time_text, old_result.next_screen)
    new_screens["rankings"].show(old_rankings.new_record)

    if old_battle.player_one is not None:
        new_screens["battle"].setup(old_battle.player_one.name, old_battle.player_two.name, old_battle.mode)
        new_screens["battle"].set_names(old_battle.player_one_name, old_battle.player_two_name)

    return new_screens


def is_reload_key(event, current_name):
    if event.type != pygame.KEYDOWN:
        return False
    if event.key == pygame.K_F5:
        return True
    if event.key == pygame.K_r and current_name not in settings.TYPING_SCREENS:
        return True
    return False


def get_player_names(screens, mode):
    player_one = screens["login"].user
    if player_one is None:
        player_one = settings.PLAYER_ONE_LABEL

    if mode == "multiplayer":
        return player_one, settings.PLAYER_TWO_LABEL
    return player_one, settings.CPU_LABEL


def finish_battle(screens, battle_start_time):
    battle = screens["battle"]
    winner = battle.get_winner()
    battle_time = time.time() - battle_start_time

    new_record = None
    pending_record = None
    next_screen = "rankings"

    if battle.human_won():
        new_record = {
            "name": battle.get_winner_owner_name(),
            "pokemon": winner.name,
            "mode": settings.MODE_NAMES[battle.mode],
            "time": round(battle_time, 1)
        }
        if battle.mode == "multiplayer" and winner is battle.player_two:
            pending_record = new_record
            new_record = None
            next_screen = "login_two"
        else:
            rankings.add_record(new_record)

    screens["result"].show(battle.get_result_title(), battle.get_result_color(), winner.name,
                           rankings.format_time(battle_time), next_screen)
    screens["rankings"].show(new_record)
    return pending_record


def save_pending_record(screens, pending_record):
    player_two = screens["login_two"].user
    if pending_record is None or player_two is None:
        screens["rankings"].show(None)
        return

    pending_record["name"] = player_two
    rankings.add_record(pending_record)
    screens["rankings"].show(pending_record)


backgrounds.load_backgrounds()
screens = create_screens()
current_name = "start"
battle_start_time = 0
pending_record = None
fade = transition.Transition()
clock = pygame.time.Clock()
running = True

resume_screen = debug_console.start(screens)
if resume_screen is not None:
    fade.start(resume_screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

        if debug_console.handle_event(event):
            continue

        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()
            continue

        if is_reload_key(event, current_name):
            screens = reload_game(screens)
            fade = transition.Transition()
            continue

        if fade.is_active():
            continue

        next_name = screens[current_name].handle_event(event)
        if next_name == "quit":
            running = False
        elif next_name is not None:
            fade.start(next_name)

    new_name = fade.update()
    if new_name == "register":
        screens["register"].reset(current_name)
    if new_name in ["login", "login_two"] and current_name == "register":
        created_user = screens["register"].created_user
        if created_user is not None:
            screens[new_name].after_register(created_user)
    if new_name == "login_two" and current_name == "result":
        screens["login_two"].reset(screens["login"].user)
    if new_name == "select":
        screens["select"].reset(screens["difficulty"].mode)
    if new_name == "rankings" and current_name == "login_two":
        save_pending_record(screens, pending_record)
        pending_record = None
    elif new_name == "rankings" and current_name != "result":
        screens["rankings"].show(None)
    if new_name == "battle":
        select = screens["select"]
        player_one_name, player_two_name = get_player_names(screens, select.mode)
        screens["battle"].start(select.player_one_choice, select.player_two_choice, select.mode)
        screens["battle"].set_names(player_one_name, player_two_name)
        battle_start_time = time.time()
    if new_name is not None and new_name != "battle":
        backgrounds.pick_new()
    if new_name is not None:
        current_name = new_name
        debug_console.remember(screens, current_name)

    sound.play_music(settings.SCREEN_MUSIC.get(current_name))

    battle = screens["battle"]

    wanted_screen = debug_console.run(screens, current_name)
    if wanted_screen is not None and not fade.is_active():
        fade.start(wanted_screen)

    if current_name == "battle" and not fade.is_active() and battle.is_over():
        pending_record = finish_battle(screens, battle_start_time)
        fade.start("result")

    screens[current_name].draw(screen)
    fade.draw(screen)
    debug_console.draw(screen)
    pygame.display.flip()
    clock.tick(settings.FPS)

pygame.quit()
