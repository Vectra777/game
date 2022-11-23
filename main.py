from random import randint
import sys
sys.path.append("global")
sys.path.append("player")
sys.path.append("ennemy")
from reprint import *
from art import text2art
from role.knight import knight
from role.elf import elf
from role.sorcerer import sorcerer
from ennemy.races.werewolf import werewolf
from ennemy.races.orc import orc
from ennemy.races.vampire import vampire

title= text2art("MYTHIC    ADVENTURE",font='epic',chr_ignore=True)
sub= text2art("tap 1 to play!",font="small",chr_ignore=True)
reprint(title)
print(f"{sub}\n")
play = int(input(""))
inventory = [0,0,0,0,0,0,0,0,0,0] 
def start():
    clear()
    name = str(input("what's your name ?: "))
    reprint(text2art("CHOOSE YOUR CHARACTER",font="small",chr_ignore=True))
    classes =  int(input("classes:\n1:knight\n2:elf\n3:sorcerer\n"))
    match classes:
        case 1:
            return knight(name,100,0,3,inventory,100,1)
        case 2:
            return elf(name,90,0,20,2,inventory,100,1)
        case 3:
            return sorcerer(name,100,0,50,1,inventory,100,1)
        case _:
            reprint("It's not a class !")
            start()

if play == 1:
    p1 = start()
else:
    print("Good bye!")
    sys.exit()
    
def game():
    reprint(text2art("READY? GO!",font="3D Diagonal",chr_ignore=True))
    match randint(0,3):
        case 1:
            enemy = werewolf("werewolf",p1.lvl*0.5+10,(p1.lvl*10**-1)+7,(p1.lvl*10**-1)+3)
        case 2:
            enemy = vampire("vampire",p1.lvl*0.5+12,8+(p1.lvl*10**-1),(p1.lvl*10**-1)+2)
        case 3:
            enemy = orc("orc",p1.lvl*0.5+20,8*(p1.lvl*10**-1)+10,(p1.lvl*10**-1)+3)