from globale import (reprint,clear,WEREWOLF,ORC,VAMPIRE,battle)
from player import *
from ennemy import *
from art import text2art
from random import randint
from time import sleep
import sys
import pandas as pd
import ast

title= text2art("MYTHIC    ADVENTURE",font='epic',chr_ignore=True)
sub= text2art("tap 1 to play!",font="small",chr_ignore=True)
clear()

reprint(title)
print(f"{sub}\n")
play = int(input(""))

inventory = [0,0,0,0,0,0,0,0,0,0]
sword=r"""
      /| ________________
O|===|* >________________>
      \|
"""

bow=r"""
   (
    \
     )
##-------->
     )
    /
   (
"""

wand = r"""
                  .

                   .
         /^\     .
    /\   "V"
   /__\   I      O  o
  //..\\  I     .
  \].`[/  I
  /l\/j\  (]    .  O
 /. ~~ ,\/I          .
 \\L__j^\/I       o
  \/--v}  I     o   .
  |    |  I   _________
  |    |  I c(`       ')o
  |    l  I   \.     ,/
_/j  L l\_!  _//^---^\\_ 
"""

def start():
    clear()
    if int(input("Would you like to continue the adventure or create a new profile ?\nContinue: 1\nNew profile: 2\n"))== 2:
        pname = input("What's your name?: ")
        print(text2art("CHOOSE YOUR CHARACTER",font="small",chr_ignore=True))
        classes =  int(input(f"{sword}\n1:knight \n\n     {bow}\n2:elf \n      {wand}\n3:sorcerer\n\nchoice:"))
        match classes:
            case 1:
                return knight("knight",100,0,0,3,inventory,100,1,pname)
            case 2:
                return elf("elf",90,0,20,2,inventory,100,1,pname)
            case 3:
                return sorcerer("sorcerer",100,0,50,1,inventory,100,1,pname)
            case _:
                reprint("It's not a class !")
                start()
    else:
        saves= pd.read_csv("save.cvs",skipinitialspace=True)
        
        match saves.iloc[1]["data"]:
            case "elf":
                return elf("elf",90,float(saves.iloc[0]["data"]),float(saves.iloc[2]["data"]),float(saves.iloc[3]["data"]),ast.literal_eval(saves.iloc[4]["data"]),float(saves.iloc[5]["data"]),float(saves.iloc[7]["data"]),saves.iloc[6]["data"])
            case "knight":
                return knight("knight",100,float(saves.iloc[0]["data"]),float(saves.iloc[2]["data"]),float(saves.iloc[3]["data"]),ast.literal_eval(saves.iloc[4]["data"]),float(saves.iloc[5]["data"]),float(saves.iloc[7]["data"]),saves.iloc[6]["data"])
            case "sorcerer":
                return sorcerer("sorcerer",100,float(saves.iloc[0]["data"]),float(saves.iloc[2]["data"]),float(saves.iloc[3]["data"]),ast.literal_eval(saves.iloc[4]["data"]),float(saves.iloc[5]["data"]),float(saves.iloc[7]["data"]),saves.iloc[6]["data"])

if play == 1:
    p1 = start()
else:
    print("Good bye!")
    sys.exit()
    
def game():
    clear()
    print(text2art("READY?     GO!",font="3D Diagonal",chr_ignore=True))
    sleep(1.5)
    match randint(1,3):
                case 1:
                    enemy = werewolf("werewolf",p1.lvl*0.5+10,(p1.lvl*10**-1)+7,0,(p1.lvl*10**-1),0,1)
                    img=WEREWOLF
                case 2:
                    enemy = vampire("vampire",p1.lvl*0.5+12,8+(p1.lvl*10**-1),0,(p1.lvl*10**-1)+3,0,1)
                    img=VAMPIRE
                case 3:
                    enemy = orc("orc",p1.lvl*0.5+20,8*(p1.lvl*10**-1)+10,0,(p1.lvl*10**-1)+3,0,1)
                    img=ORC
                    
    battle(enemy,img,p1)
    
    if int(input("Do you want to play again?\n1:Yes\n2:No\n")) == 1:
            game()
    else:
        save = pd.DataFrame({
            "data_type":["xp","class","mana","power","inv","xpmax","pname","lvl"],
            "data":[p1.xp,p1.name,p1.mana,p1.str,p1.inv,p1.xpmax,p1.pname,p1.lvl]
        })
        save.to_csv("save.cvs",index=False)
        clear()
        print("Ok Bye!")
        sleep(2.5)
game()