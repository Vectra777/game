from ennemy import ennemy
import sys
sys.path.append("global")
from reprint import reprint

class orc(ennemy):
    def __init__(self, name:str, hp:int, xp:int, str:int):
        super().__init__(name, hp, xp, str)
    
    def dmg(self,entity):
        super().dmg(entity)
    
    def fall(self,entity):
        reprint("The tought falling on the ground was the best way to attack you.")
        entity.hp = entity.hp-self.hp*(10**-1)