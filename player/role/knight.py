import sys
sys.path.append("player")
sys.path.append("global")
from player import player
from reprint import (reprint,clear)
from player import player
from random import randint

class knight(player):
    def __init__(self, name: str, hp: int, xp: int, str: int, inv: list, xpmax: int, lvl: int):
        super().__init__(name, hp, xp, str, inv, xpmax, lvl)
    
    def dmg(self,entity):
        super().dmg(entity)
    
    def seeinv(self):
        super().seeinv()
    
    def win(self,entity):
        super.win(entity)
    
    def lose(self):
        super().lose()
    
    def vertical_slash(self,entity):
        if randint(1,5) == 5:
            reprint("You sliced your opponent!")
            entity.hp = entity.hp-self.str*2
            reprint(f"{entity.name} a pris {self.str*2} dégas !")
        else:
            reprint("You slash wasn't so good...")
            super().dmg()