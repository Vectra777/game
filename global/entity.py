from reprint import *
class Entity:
    def __init__(self,name:str,hp:int,xp:int,mana:int,str:int,xpmax:int,lvl:int):
        self.mana = mana
        self.name = name
        self.hp = hp
        self.xp = xp
        self.str = str
        self.xpmax = xpmax
        self.lvl  = lvl
    
    def dmg(self,entity):
        entity.hp = entity.hp-self.str
        reprint(f"{entity.name} a pris {self.str} dégas !")