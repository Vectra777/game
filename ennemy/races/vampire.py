import sys
sys.path.append("global")
from reprint import reprint
from ennemy import ennemy

class vampire(ennemy):
    def __init__(self, name:str, hp:int, xp:int, str:int):
        super().__init__(name, hp, xp, str)
    
    def dmg(self,entity):
        super().dmg(entity)
    
    def vampirism(self,entity):
        reprint("the vampire sucked your blood!")
        entity.hp = entity.hp - self.str
        self.hp = self.hp + self.str