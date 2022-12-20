from player.player import player
from random import randint
from time import sleep

class sorcerer(player):
    def __init__(self, name: str, hp: int, xp: int, mana: int, str: int, inv: list, xpmax: int, lvl: int,pname:str):
        super().__init__(name, hp, xp, mana, str, inv, xpmax, lvl, pname)
        
    def dmg(self,entity):
        super().dmg(entity)
    
    def seeinv(self):
        super().seeinv()
    
    def win(self,entity):
        super().win(entity)
    
    def lose(self):
        super().lose()
    
    def spell(self,entity):
        
        choice = int(input("\nchoose the spell:\n   1:fire ball\n   2:heal\n   3:wind slice\n   4:augment\n   5:depression\n\n"))
        
        match choice:
            case 1:
                atk= self.str*(randint(1,self.lvl)*(10**-1)+1)
                self.mana = self.mana-30
                entity.hp = round(entity.hp - atk,1)
                print("FIRE BALL!")
                print(f"{entity.name} took {atk} fire damages!")
                

            case 2:
                heal_lvl = int(input(f"choose a heal level:\n   1: smol heal (restore 10% hp and need {self.mana*0.1} mana points)\n   2:mid heal (40% hp and need {self.mana*0.4} mana points)\n   3:BIG heal (70% hp and need {self.mana*0.7} mana points)"))
                if heal_lvl == 1:
                    self.mana = self.mana*0.1
                    self.hp = round(self.hp*1.1,1)
                    print(f"You now have {self.hp} hp")
            case 3:
                atk= self.lvl*(randint(10,50))
                self.mana = self.mana-40
                entity.hp = round(entity.hp - atk,0)
                print("\nWIND SLICE!")
                sleep(2)
                print(f"{entity.name} took {atk} wind damage!")
            case 4:
                print("you used augment!")
                self.mana = self.mana-15
                self.str = round(self.str*1.5,1)
                sleep(1.5)
            case 5:
                self.mana = self.mana-10
                print(f"you used depression and the {entity.name} is crying (less power)!")
                entity.str = round(entity.str*0.8,1)