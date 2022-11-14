import sys
sys.path.append("player")
sys.path.append("global")
from player import player
from reprint import (reprint,clear)
from player import player
from random import randint

class elf(player):
    def __init__(self, name: str, hp: int, xp: int, mana: int, str: int, inv: list, xpmax: int, lvl: int):
        super().__init__(name, hp, xp, mana, str, inv, xpmax, lvl)