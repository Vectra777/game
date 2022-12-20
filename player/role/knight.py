from player.player import player
from random import randint

class knight(player):
    def __init__(self, name: str, hp: int, xp: int,mana: int, str: int, inv: list, xpmax: int, lvl: int,pname:str):
        super().__init__(name, hp, xp, mana, str, inv, xpmax, lvl,pname)
    
    def dmg(self,entity):
        super().dmg(entity)
    
    def seeinv(self):
        super().seeinv()
    
    def win(self,entity):
        super().win(entity)
    
    def lose(self):
        super().lose()
    
    def vertical_slash(self,entity):
        if randint(1,5) == 5:
            print("\nYou sliced your opponent!")
            entity.hp = round(entity.hp-self.str*2,1)
            print(f"{entity.name} took {self.str*2} of slicing damage !")
        else:
            print("\nYou slash wasn't so good...")
            super().dmg(entity)