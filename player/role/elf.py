import sys
sys.path.append("player")
sys.path.append("global")
from player import player
from reprint import (reprint)
from random import randint

class elf(player):
    def __init__(self, name: str, hp: int, xp: int, mana: int, str: int, inv: list, xpmax: int, lvl: int):
        super().__init__(name, hp, xp, mana, str, inv, xpmax, lvl)
        
    def dmg(self,entity):
        super().dmg(entity)
    
    def seeinv(self):
        super().seeinv()
    
    def win(self,entity):
        super.win(entity)
    
    def lose(self):
        super().lose()
        
    def bow_shot(self,entity):
        acc = self.lvl+50
        if randint(0,100) <=acc:
            reprint("nice shot!")
            entity.hp = entity.hp - self.str*2
    
    