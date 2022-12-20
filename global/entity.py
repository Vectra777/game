from time import sleep
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
        entity.hp = round(entity.hp-self.str,1)
        sleep(1)
        print(f"{entity.name} took {self.str} damages !\n")
        sleep(2)