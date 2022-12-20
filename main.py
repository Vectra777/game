from globale import (reprint,clear,WEREWOLF,ORC,VAMPIRE,battle)
from player import *
from ennemy import *
from art import text2art
from random import randint
from time import sleep
import sys

title= text2art("MYTHIC    ADVENTURE",font='epic',chr_ignore=True)
sub= text2art("tap 1 to play!",font="small",chr_ignore=True)
clear()

reprint(title)
print(f"{sub}\n")
play = int(input(""))

inventory = [0,0,0,0,0,0,0,0,0,0] 

def start():
    clear()
    pname = input("What's your name?: ")
    print(text2art("CHOOSE YOUR CHARACTER",font="small",chr_ignore=True))
    classes =  int(input("classes:\n1:knight\n2:elf\n3:sorcerer\n"))
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
        save = open("save.txt","w")
        xp_str=str(p1.xp)
        save.writelines(["xp = "+ xp_str + "\n",])
        save.close()
        clear()
        print("Ok Bye!")
        sleep(2.5)
game()