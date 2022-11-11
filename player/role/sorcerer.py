from player.player import *

class sorcerer(player):
    def __init__(self, name: str, hp: int, xp: int, mana: int, str: int, inv: list, xpmax: int, lvl: int):
        super().__init__(name, hp, xp, mana, str, inv, xpmax, lvl)