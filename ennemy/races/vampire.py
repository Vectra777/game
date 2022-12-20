from time import sleep
from ennemy.ennemy import ennemy

class vampire(ennemy):
    def __init__(self, name:str,hp:int,xp:int,mana:int,str:int,xpmax:int,lvl:int):
        super().__init__(name, hp, xp, str,mana,xpmax,lvl)
    
    def dmg(self,entity):
        super().dmg(entity)
    
    def vampirism(self,entity):
        print("\nThe vampire sucked your blood!")
        entity.hp = round(entity.hp - self.str,1)
        self.hp = round(self.hp + self.str,1)
        sleep(2)