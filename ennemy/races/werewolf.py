from ennemy.ennemy import ennemy
from time import sleep

class werewolf(ennemy):
    def __init__(self, name:str,hp:int,xp:int,mana:int,str:int,xpmax:int,lvl:int):
        super().__init__(name, hp, xp, str,mana,xpmax,lvl)
    
    def dmg(self,entity):
        super().dmg(entity)
    
    def bite(self,entity):
        print("\nThe werewolf just bited you and gave you aids!")
        sleep(2)
        print("You are now less powerful!")
        entity.str = round(entity.str - self.str*(10**-1),1)
        sleep(2)