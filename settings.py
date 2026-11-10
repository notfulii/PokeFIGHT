WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
CENTER_X = 640
GAME_TITLE = "PokeFIGHT"
TYPING_SCREENS = ["login", "login_two", "register"]
FPS = 60
START_FULLSCREEN = False

TRANSITION_TIME = 400
TRANSITION_COLOR = (0, 0, 0)

POKEMON_NAMES = ["Pikachu", "Charizard", "Vaporeon", "Bulbasaur", "Squirtle", "Greninja", "Eevee", "Mewtwo",
                 "Lucario", "Gengar", "Snorlax", "Rattata", "Jigglypuff", "Dragonite", "Rayquaza", "Blastoise"]

# Text and buttons
TEXT_COLOR = (255, 255, 255)
SHADOW_COLOR = (0, 0, 0)
SHADOW_OFFSET = 2
BUTTON_COLOR = (200, 40, 40)
BUTTON_BORDER_COLOR = (255, 255, 255)
BUTTON_BORDER_WIDTH = 4
BUTTON_RADIUS = 10
HOVER_COLOR = (255, 204, 0)
EXIT_TEXT = "Exit"

# Start menu
START_TITLE_WIDTH = 500
START_TITLE_HEIGHT = 500
START_TITLE_POSITION = (390, 40)
START_TEXT = "Press ENTER to start"
START_TEXT_SIZE = 32
START_TEXT_Y = 600
BLINK_TIME = 500

# Legal notice
LEGAL_LINES = [
    "Unofficial non-commercial fan project. Not affiliated with or endorsed by Nintendo, The Pokemon Company or GAME FREAK.",
    "Pokemon and all character names are trademarks of Nintendo, Creatures Inc. and GAME FREAK inc. (c) 1995-2026 Nintendo."
]
LEGAL_TEXT_SIZE = 12
LEGAL_FIRST_Y = 666
LEGAL_LINE_GAP = 18
LEGAL_COLOR = (230, 230, 230)

# Login
LOGIN_TEXT_SIZE = 20
LOGIN_TITLE = "Login"
LOGIN_TWO_TITLE = "Player 2 won! Log in to save your win"
LOGIN_TITLE_Y = 120
LOGIN_USER_LABEL = "User"
LOGIN_USER_LABEL_Y = 225
LOGIN_PASSWORD_LABEL = "Password"
LOGIN_PASSWORD_LABEL_Y = 325
LOGIN_MESSAGE_Y = 670

INPUT_X = 440
INPUT_USER_Y = 260
INPUT_PASSWORD_Y = 360
INPUT_WIDTH = 400
INPUT_HEIGHT = 50
INPUT_MAX_LENGTH = 16
INPUT_COLOR = (120, 120, 120)
INPUT_ACTIVE_COLOR = (255, 204, 0)
INPUT_BACKGROUND_COLOR = (255, 255, 255)
INPUT_TEXT_COLOR = (0, 0, 0)
INPUT_TEXT_PADDING = 12
INPUT_BORDER_WIDTH = 3
INPUT_RADIUS = 8
PASSWORD_CHARACTER = "*"

LOGIN_BUTTON_TEXT = "Login"
LOGIN_BUTTON_POSITION = (440, 460)
CREATE_ACCOUNT_TEXT = "Create account"
CREATE_ACCOUNT_POSITION = (650, 460)
BACK_TEXT = "Back"
LOGIN_BUTTON_WIDTH = 190
LOGIN_BUTTON_HEIGHT = 50

PASSWORD_MIN_LENGTH = 4
PASSWORD_HASH_ITERATIONS = 100000
SALT_SIZE = 16
MESSAGE_EMPTY_FIELDS = "Fill in both fields"
MESSAGE_WRONG_LOGIN = "Wrong username or password"
MESSAGE_SHORT_PASSWORD = "Password must have 4+ characters"
MESSAGE_ACCOUNT_CREATED = "Account created, now log in"
MESSAGE_USER_EXISTS = "That user already exists"
MESSAGE_ONLY_SPACES = "User and password can't be only spaces"
MESSAGE_PASSWORDS_DIFFERENT = "The passwords don't match"
MESSAGE_SAME_ACCOUNT = "Player 2 must use a different account"

# Exit buttons
EXIT_WIDTH = 190
EXIT_HEIGHT = 50
EXIT_TEXT_SIZE = 25
LOGIN_EXIT_POSITION = (540, 520)
SELECT_EXIT_POSITION = (180, 630)

# Change mode buttons
CHANGE_BUTTON_POSITION = (160, 540)
CHANGE_WIDTH = 230
CHANGE_HEIGHT = 50
CHANGE_TEXT_SIZE = 24
CHANGE_MODE_BUTTON_TEXT = "Change Mode"
CHANGE_BUTTON_COLOR = (90, 0, 163)

# Rank Button
RANK_BUTTON_POSITION = (1170, 650)
RANK_WIDTH = 50
RANK_HEIGHT = 50
RANK_BUTTON_COLOR = (255, 0, 0)
RANK_ICON_SIZE = 36

# Difficulty
MODE_TITLE = "Choose difficulty"
MODE_TITLE_Y = 150
MODE_TEXT_SIZE = 32
MODE_BUTTON_X = 490
MODE_BUTTON_WIDTH = 300
MODE_BUTTON_HEIGHT = 80
MODE_EASY_Y = 260
MODE_HARD_Y = 380
MODE_MULTIPLAYER_Y = 500
EASY_TEXT = "Easy"
HARD_TEXT = "Hard"
MULTIPLAYER_TEXT = "Multiplayer"
EASY_COLOR = (40, 160, 60)
HARD_COLOR = (200, 40, 40)
MULTIPLAYER_COLOR = (9, 112, 230)

# Register
REGISTER_TITLE = "Create account"
REGISTER_TITLE_Y = 90
REGISTER_USER_LABEL_Y = 175
REGISTER_USER_Y = 210
REGISTER_PASSWORD_LABEL_Y = 275
REGISTER_PASSWORD_Y = 310
REGISTER_CONFIRM_LABEL = "Repeat password"
REGISTER_CONFIRM_LABEL_Y = 375
REGISTER_CONFIRM_Y = 410
REGISTER_BUTTON_TEXT = "Register"
REGISTER_BUTTON_POSITION = (440, 490)
REGISTER_BACK_POSITION = (650, 490)
REGISTER_BUTTON_COLOR = (40, 160, 60)
REGISTER_MESSAGE_Y = 590

# Select
SELECT_TITLE_WIDTH = 370
SELECT_TITLE_HEIGHT = 370
SELECT_TITLE_POSITION = (100, 50)
SELECT_TEXT = "Select your pokemon"
SELECT_PLAYER_ONE_TEXT = "Player 1: select"
SELECT_PLAYER_TWO_TEXT = "Player 2: select"
SELECT_READY_TEXT = "Ready! Press Play"

PLAYER_ONE_COLOR = (220, 40, 40)
PLAYER_TWO_COLOR = (40, 110, 230)
PERSON_SIZE = 24
PERSON_OUTLINE_COLOR = (255, 255, 255)
PERSON_OUTLINE_WIDTH = 2
PERSON_ONE_OFFSET = (16, 6)
PERSON_TWO_OFFSET = (94, 6)
PERSON_BOUNCE = 4
PERSON_BOUNCE_SPEED = 250

PLAY_TEXT = "Play"
PLAY_TEXT_SIZE = 32
PLAY_BUTTON_POSITION = (160, 460)
PLAY_WIDTH = 230
PLAY_HEIGHT = 60
PLAY_COLOR = (40, 160, 60)
PLAY_DISABLED_COLOR = (90, 90, 90)
SELECT_TEXT_SIZE = 40
SELECT_TEXT_POSITION = (680, 100)
GRID_X = 650
GRID_Y = 200
COLUMNS = 4
ROWS = 4
CELL_SIZE = 120
BOX_SIZE = 110
BOX_COLOR = (82, 82, 82, 120)
BOX_BORDER_COLOR = (255, 255, 255)
BOX_BORDER_WIDTH = 3
BOX_RADIUS = 12


# Sprites
SELECT_SPRITE_SIZE = 90
PLAYER_SPRITE_SIZE = 200
ENEMY_SPRITE_SIZE = 150
PLAYER_FEET = (400, 600)
ENEMY_FEET = (850, 400)
GIF_DEFAULT_FRAME_TIME = 100
GIF_MIN_FRAME_TIME = 50
STILL_FRAME_TIME = 1000

PLAYER_SIZE_OVERRIDES = {
    "Mewtwo": 350,
    "Rayquaza": 370,
    "Lucario": 250,
    "Dragonite": 300,
    "Greninja": 220,
    "Vaporeon": 210,
    "Gengar": 250,
    "Charizard": 300,
    "Blastoise": 270,
    "Mew": 200,
    "Snorlax": 300
}

ENEMY_SIZE_OVERRIDES = {
    "Mewtwo": 300,
    "Rayquaza": 350,
    "Lucario": 200,
    "Dragonite": 250,
    "Greninja": 220,
    "Vaporeon": 170,
    "Gengar": 200,
    "Charizard": 250,
    "Blastoise": 220,
    "Mew": 200,
    "Snorlax": 200
}

# Battle
BATTLE_TEXT_SIZE = 24
DOCK_SIZE = 300
PLAYER_DOCK_POSITION = (900, 400)
ENEMY_DOCK_POSITION = (100, 0)
PLAYER_NAME_POSITION = (1055, 520)
ENEMY_NAME_POSITION = (255, 120)

PLAYER_HEALTH_BAR = (1014, 583, 144, 6)
ENEMY_HEALTH_BAR = (214, 183, 144, 6)
HEALTH_GREEN = (112, 248, 168)
HEALTH_YELLOW = (248, 224, 56)
HEALTH_RED = (208, 40, 40)
HEALTH_YELLOW_BELOW = 0.5
HEALTH_RED_BELOW = 0.2

TURN_TEXT_SIZE = 28
TURN_TEXT_Y = 20
TURN_TEXT_COLOR = (0, 136, 255)
MODE_LABEL_Y = 55
PLAYER_ONE_LABEL = "Player 1"
PLAYER_TWO_LABEL = "Player 2"
YOU_LABEL = "You"
CPU_LABEL = "CPU"
MODE_NAMES = {
    "easy": "Easy",
    "hard": "Hard",
    "multiplayer": "Multiplayer"
}

LUNGE_TIME = 250
RETURN_TIME = 300
HIT_TIME = 500
ATTACK_TOTAL_TIME = 800
LUNGE_PERCENT = 0.35
SHAKE_DISTANCE = 8
SHAKE_SPEED = 50
FLASH_SPEED = 100
HIT_RED = (180, 0, 0)
HP_DRAIN_PER_FRAME = 0.5

EASY_CPU_DAMAGE = 0.8
HARD_CPU_DAMAGE = 1.25

EASY_PLAYER_HP = 1.15
EASY_CPU_HP = 0.9
HARD_PLAYER_HP = 1.0
HARD_CPU_HP = 1.4
MULTIPLAYER_HP = 1.6
MULTIPLAYER_MAX_HIT = 0.18
SINGLE_PLAYER_MAX_HIT = 0.6

CRIT_CHANCE = 0.0625
CRIT_MULTIPLIER = 1.5
CRIT_TEXT = "Critical hit!"
SUPER_EFFECTIVE_TEXT = "Super effective!"
NOT_EFFECTIVE_TEXT = "Not very effective..."
NO_EFFECT_TEXT = "It had no effect..."

TYPE_CHART = {
    "normal": {"rock": 0.5, "ghost": 0, "steel": 0.5},
    "fire": {"fire": 0.5, "water": 0.5, "grass": 2, "ice": 2, "bug": 2, "rock": 0.5, "dragon": 0.5, "steel": 2},
    "water": {"fire": 2, "water": 0.5, "grass": 0.5, "ground": 2, "rock": 2, "dragon": 0.5},
    "electric": {"water": 2, "electric": 0.5, "grass": 0.5, "ground": 0, "flying": 2, "dragon": 0.5},
    "grass": {"fire": 0.5, "water": 2, "grass": 0.5, "poison": 0.5, "ground": 2, "flying": 0.5, "bug": 0.5,
              "rock": 2, "dragon": 0.5, "steel": 0.5},
    "ice": {"fire": 0.5, "water": 0.5, "grass": 2, "ice": 0.5, "ground": 2, "flying": 2, "dragon": 2, "steel": 0.5},
    "fighting": {"normal": 2, "ice": 2, "poison": 0.5, "flying": 0.5, "psychic": 0.5, "bug": 0.5, "rock": 2,
                 "ghost": 0, "dark": 2, "steel": 2, "fairy": 0.5},
    "poison": {"grass": 2, "poison": 0.5, "ground": 0.5, "rock": 0.5, "ghost": 0.5, "steel": 0, "fairy": 2},
    "ground": {"fire": 2, "electric": 2, "grass": 0.5, "poison": 2, "flying": 0, "bug": 0.5, "rock": 2, "steel": 2},
    "flying": {"electric": 0.5, "grass": 2, "fighting": 2, "bug": 2, "rock": 0.5, "steel": 0.5},
    "psychic": {"fighting": 2, "poison": 2, "psychic": 0.5, "dark": 0, "steel": 0.5},
    "bug": {"fire": 0.5, "grass": 2, "fighting": 0.5, "poison": 0.5, "flying": 0.5, "psychic": 2, "ghost": 0.5,
            "dark": 2, "steel": 0.5, "fairy": 0.5},
    "rock": {"fire": 2, "ice": 2, "fighting": 0.5, "ground": 0.5, "flying": 2, "bug": 2, "steel": 0.5},
    "ghost": {"normal": 0, "psychic": 2, "ghost": 2, "dark": 0.5},
    "dragon": {"dragon": 2, "steel": 0.5, "fairy": 0},
    "dark": {"fighting": 0.5, "psychic": 2, "ghost": 2, "dark": 0.5, "fairy": 0.5},
    "steel": {"fire": 0.5, "water": 0.5, "electric": 0.5, "ice": 2, "rock": 2, "steel": 0.5, "fairy": 2},
    "fairy": {"fire": 0.5, "fighting": 2, "poison": 0.5, "dragon": 2, "dark": 2, "steel": 0.5}
}

MOVES_PER_POKEMON = 4
BACKUP_MOVE = {"name": "struggle", "power": 50, "type": "typeless", "damage_class": "physical"}
HP_BONUS = 60
DAMAGE_MULTIPLIER = 2
POWER_DIVIDER = 10
MIN_DAMAGE = 1

PANEL_POSITION = (40, 630)
PANEL_WIDTH = 1200
PANEL_HEIGHT = 80
PANEL_COLOR = (20, 20, 20, 180)
PANEL_RADIUS = 12
MESSAGE_POSITION = (70, 658)

MOVE_BUTTON_POSITIONS = [(70, 640), (360, 640), (650, 640), (940, 640)]
MOVE_BUTTON_WIDTH = 270
MOVE_BUTTON_HEIGHT = 60

TYPE_COLORS = {
    "normal": (168, 168, 120),
    "fire": (240, 128, 48),
    "water": (104, 144, 240),
    "electric": (232, 192, 0),
    "grass": (120, 200, 80),
    "ice": (120, 200, 200),
    "fighting": (192, 48, 40),
    "poison": (160, 64, 160),
    "ground": (200, 160, 80),
    "flying": (168, 144, 240),
    "psychic": (248, 88, 136),
    "bug": (168, 184, 32),
    "rock": (184, 160, 56),
    "ghost": (112, 88, 152),
    "dragon": (112, 56, 248),
    "dark": (112, 88, 72),
    "steel": (184, 184, 208),
    "fairy": (238, 153, 172)
}

# Result
RESULT_TITLE_SIZE = 80
RESULT_TEXT_SIZE = 32
RESULT_TITLE_Y = 260
RESULT_WINNER_Y = 340
WIN_TEXT = "YOU WIN"
LOSE_TEXT = "YOU LOSE"
PLAYER_ONE_WINS_TEXT = "PLAYER 1 WINS"
PLAYER_TWO_WINS_TEXT = "PLAYER 2 WINS"
WIN_COLOR = (0, 255, 0)
LOSE_COLOR = (200, 40, 40)
RESULT_TEXT = "Press ENTER to continue"
RESULT_TEXT_Y = 560
WINS_TEXT = "WINS"
RESULT_TIME_Y = 400
RESULT_TIME_COLOR = (255, 204, 0)

# Rankings
RANKING_TITLE = "RANKINGS"
RANKING_TITLE_SIZE = 56
RANKING_TITLE_Y = 40
RANKING_TEXT_SIZE = 26
RANKING_SIZE = 10
RANKING_PANEL_POSITION = (160, 120)
RANKING_PANEL_WIDTH = 960
RANKING_PANEL_HEIGHT = 480
RANKING_PANEL_COLOR = (20, 20, 20, 180)
RANKING_PANEL_RADIUS = 12
RANKING_HEADERS = ["#", "Player", "Pokemon", "Mode", "Time"]
RANKING_COLUMNS_X = [200, 270, 560, 800, 990]
RANKING_HEADER_Y = 140
RANKING_FIRST_ROW_Y = 190
RANKING_ROW_GAP = 40
RANKING_HEADER_COLOR = (255, 204, 0)
RANKING_NEW_COLOR = (112, 248, 168)
RANKING_EMPTY_TEXT = "No wins yet"
RANKING_CONTINUE_Y = 640

# Internet
POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/"
MOVE_URL = "https://pokeapi.co/api/v2/move/"
REQUEST_TIMEOUT = 10

# Files
FOLDER_ANIM_FRONT = "assets/sprites/anim_front"
FOLDER_ANIM_BACK = "assets/sprites/anim_back"
FOLDER_FRONT = "assets/sprites/frontpokes"
FOLDER_BACK = "assets/sprites/backpokes"
FOLDER_DATA = "assets/data"
FOLDER_BACKGROUNDS = "assets/backgrounds"
FIRST_BACKGROUND = "select_poke.jpg"
BATTLE_BACKGROUND = "background_fight.png"
BACKGROUND_FIGHT = "assets/backgrounds/background_fight.png"
TITLE_IMAGE = "assets/layout/title.png"
TEXT_FONT = "assets/fonts/Minecraft.ttf"
DOCK_IMAGE = "assets/layout/dock.png"
OVER_DOCK_IMAGE = "assets/layout/over_dock.png"
USERS_FILE = "assets/data/users.json"
STATS_FILE = "assets/data/stats.json"
MOVES_FILE = "assets/data/moves.json"
RANKINGS_FILE = "assets/data/rankings.json"
DEBUG_FILE = "assets/data/debug_state.json"

# Debug console
DEBUG_ON = True
DEBUG_RESUME = False
DEBUG_DEFAULT_MODE = "easy"
DEBUG_KEYS = ["`", "f1"]
DEBUG_PANEL_HEIGHT = 330
DEBUG_PANEL_COLOR = (0, 0, 0, 210)
DEBUG_FONT = "consolas,dejavusansmono"
DEBUG_TEXT_SIZE = 16
DEBUG_TEXT_COLOR = (200, 255, 200)
DEBUG_INPUT_COLOR = (255, 204, 0)
DEBUG_MAX_LINES = 14
DEBUG_LINE_GAP = 20
DEBUG_MARGIN = 12
DEBUG_HELP = [
    "` or F1                   open / close this console (Esc also closes it)",
    "help                      show this list",
    "screens                   list the screen names",
    "where                     say which screen you are in",
    "go <screen>               jump to a screen (go battle, go select, go rankings...)",
    "mode <easy|hard|multiplayer>",
    "pick <pokemon> [pokemon]  choose the pokemon for player 1 and player 2",
    "names <name>              set the player 1 account name",
    "enemy <amount>            hurt the top pokemon (battle only)",
    "player <amount>           hurt the bottom pokemon (battle only)",
    "heal                      heal both (battle only)",
    "win / lose                end the battle now (battle only)",
    "forget                    stop resuming the last screen"
]

# Sound
SOUND_ON = True
MUSIC_VOLUME = 0.2
CRY_VOLUME = 0.1
FOLDER_CRIES = "assets/sounds/cries"
MENU_MUSIC = "assets/music/menu.mp3"
BATTLE_MUSIC = "assets/music/battle.ogg"
VICTORY_MUSIC = "assets/music/victory.ogg"
SCREEN_MUSIC = {
    "start": MENU_MUSIC,
    "login": MENU_MUSIC,
    "difficulty": MENU_MUSIC,
    "login_two": MENU_MUSIC,
    "register": MENU_MUSIC,
    "select": MENU_MUSIC,
    "battle": BATTLE_MUSIC,
    "result": VICTORY_MUSIC,
    "rankings": VICTORY_MUSIC
}
RANKING_IMAGE = "assets/layout/trophy.png"
