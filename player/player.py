from globale import (Entity,reprint)
from time import sleep

class player (Entity):
    def __init__(self, name:str, hp:int, xp:int, mana:int, str:int,inv:list,xpmax:int,lvl:int,pname:str):
        self.inv = inv
        self.pname = pname
        super().__init__(name, hp, xp, mana, str,xpmax,lvl)
        
    def dmg(self,entity):
        super().dmg(entity)
    
    def see_inv(self):
        reprint(self.inv)
    
    def win(self,entity):
        print("\nyou won!")
        self.xp = self.xp + entity.xp
        print(f"you gained {entity.xp} xp!\n{self.xpmax-self.xp} xp left until next level.")
        sleep(2)
        
    def lose(self):
        reprint("You losed to a mob (cringe.)")
        sleep(2)
