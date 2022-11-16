import sys
sys.path.append("global")
from entity import *
class player (Entity):
    def __init__(self, name:str, hp:int, xp:int, str:int):
        super().__init__(name, hp, xp, str)
    
    def dmg(self,entity):
        super().dmg(entity)