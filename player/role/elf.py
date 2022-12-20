from time import sleep
from player.player import player
from random import randint

class elf(player):
    def __init__(self, name: str, hp: int, xp: int, mana: int, str: int, inv: list, xpmax: int, lvl: int,pname:str):
        super().__init__(name, hp, xp, mana, str, inv, xpmax, lvl,pname)
        
    def dmg(self,entity):
        super().dmg(entity)
    
    def seeinv(self):
        super().seeinv()
    
    def win(self,entity):
        super().win(entity)
    
    def lose(self):
        super().lose()
        
    def bow_shot(self,entity):
        acc = self.lvl+50
        if randint(0,100) <=acc:
            print("\nnice shot!")
            entity.hp = round(entity.hp - self.str*2,1)
            sleep(1.5)
        else:
            print("\nyou missed!")
    
    