import sys
from ennemy.ennemy import ennemy
from time import sleep
sys.path.append("global")
from reprint import reprint

class werewolf(ennemy):
    def __init__(self, name:str, hp:int, xp:int, str:int):
        super().__init__(name, hp, xp, str)
    
    def dmg(self,entity):
        super().dmg(entity)
    
    def bite(self,entity):
        reprint("The werewolf just bited you and gave you aids!")
        sleep(2)
        reprint("You are now less powerful!")
        entity.str = entity.str - self.str*(10**-1)