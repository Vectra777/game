import sys
sys.path.append("global")
sys.path.append("player")
from reprint import *
from player import *
from random import randint
from time import sleep

class sorcerer(player):
    def __init__(self, name: str, hp: int, xp: int, mana: int, str: int, inv: list, xpmax: int, lvl: int):
        super().__init__(name, hp, xp, mana, str, inv, xpmax, lvl)
        
    def dmg(self,entity):
        super().dmg(entity)
    
    def seeinv(self):
        super().seeinv()
    
    def win(self,entity):
        super.win(entity)
    
    def lose(self):
        super().lose()
    
    def spell(self,entity):
        
        clear()
        choice = int(input("choose the spell:\n   1:fire ball\n   2:heal\n   3:wind slice\n   4:augment\n   5:depression"))
        
        match choice:
            case 1:
                atk= self.str*(randint(1,self.lvl)*(10**-1)+1)
                self.mana = self.mana-30
                entity.hp = entity.hp - atk
                reprint("FIRE BALL!")
                sleep(2)
                reprint(f"{entity.name} a pris {atk} dégat de feux!")

            case 2:
                heal_lvl = int(input(f"choose a heal level:\n   1: smol heal (restore 10% hp and need {self.mana*0.1} mana points)\n   2:mid heal (40% hp and need {self.mana*0.4} mana points)\n   3:BIG heal (70% hp and need {self.mana*0.7} mana points)"))
                if heal_lvl == 1:
                    self.mana = self.mana*0.1
                    self.hp = self.hp*1.1
                    reprint(f"You now have {self.hp} hp")
            case 3:
                atk= self.lvl*(randint(10,50))
                self.mana = self.mana-40
                entity.hp = entity.hp - atk
                reprint("FIRE BALL!")
                sleep(2)
                reprint(f"{entity.name} a pris {atk} dégat de vent!")
            case 4:
                reprint("you used augment!")
                self.str = self.str*1.5
            case 5:
                reprint(f"you used depression and the f{entity.name} is crying (less power)!")
                entity.str = entity.str*0.8