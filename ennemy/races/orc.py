from time import sleep
from ennemy.ennemy import ennemy

class orc(ennemy):
    def __init__(self, name:str,hp:int,xp:int,mana:int,str:int,xpmax:int,lvl:int):
        super().__init__(name, hp, xp, str,mana,xpmax,lvl)
    
    def dmg(self,entity):
        super().dmg(entity)
    
    def fall(self,entity):
        print("\nHe tought falling on the ground was the best way to attack you.")
        entity.hp = round(entity.hp-self.hp*(10**-1),1)
        sleep(2)