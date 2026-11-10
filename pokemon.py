import settings


class Pokemon:
    def __init__(self, name, types, stats, moves, menu_image, back_frames, front_frames, cry):
        self.name = name
        self.types = types
        self.moves = moves

        self.base_max_hp = stats["hp"] + settings.HP_BONUS
        self.max_hp = self.base_max_hp
        self.current_hp = self.max_hp
        self.shown_hp = self.max_hp
        self.attack = stats["attack"]
        self.defense = stats["defense"]
        self.sp_attack = stats["special-attack"]
        self.sp_defense = stats["special-defense"]
        self.speed = stats["speed"]

        self.menu_image = menu_image
        self.back_frames = back_frames
        self.front_frames = front_frames
        self.cry = cry

    def get_effectiveness(self, move, target):
        effectiveness = 1
        move_chart = settings.TYPE_CHART.get(move["type"], {})

        for target_type in target.types:
            effectiveness = effectiveness * move_chart.get(target_type, 1)

        return effectiveness

    def calculate_damage(self, target, move):
        if move["damage_class"] == "special":
            attack = self.sp_attack
            defense = target.sp_defense
        else:
            attack = self.attack
            defense = target.defense

        effectiveness = self.get_effectiveness(move, target)
        if effectiveness == 0:
            return 0

        damage = (attack / defense) * (move["power"] / settings.POWER_DIVIDER) * settings.DAMAGE_MULTIPLIER
        damage = int(damage * effectiveness)

        if damage < settings.MIN_DAMAGE:
            damage = settings.MIN_DAMAGE
        return damage

    def set_battle_hp(self, multiplier):
        self.max_hp = int(self.base_max_hp * multiplier)
        self.heal()

    def take_damage(self, amount):
        self.current_hp = self.current_hp - amount
        if self.current_hp < 0:
            self.current_hp = 0

    def heal(self):
        self.current_hp = self.max_hp
        self.shown_hp = self.max_hp

    def is_fainted(self):
        return self.current_hp == 0
