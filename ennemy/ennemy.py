from globale import Entity
class ennemy (Entity):
    def __init__(self, name:str,hp:int,xp:int,mana:int,str:int,xpmax:int,lvl:int):
        super().__init__(name, hp, xp, str,mana,xpmax,lvl)
    
    def dmg(self,entity):
        super().dmg(entity)