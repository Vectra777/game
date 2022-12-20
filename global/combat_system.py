from random import randint
from globale import (clear)
from ennemy import *
from time import sleep
ORC=r"""
                        _,.---''```````'-.
                    ,-'`                  `-._
                 ,-`                   __,-``,\
                /             _       /,'  ,|/ \
              ,'         ,''-<_`'.    |  ,' |   \
             /          / _    `  `.  | / \ |\  |
             |         (  |`'-,---, `'  \_|/ |  |
             |         |`  \  \|  /  __,    _ \ |
             |         |    `._\,'  '    ,-`_\ \|
             |         |        ,----      /|   )
             \         \       / --.      {/   /|
              \         | |       `.\         / |
               \        / `-.                 | /
                `.     |     `-        _,--V`)\/        _,-
                  `,   |           /``V_,.--`  \.  _,-'`
                   /`--'`._        `-'`         )`'
                  /        `-.            _,.-'`
                              `-.____,.-'`
                              
"""
                              
VAMPIRE=r"""

                 /######\
               /##########\
              /   \###/    \
             /     \#/      \
          /\|               |/\
          | | \ ==\    /== / | |
           \|  \<|>\  /<|>/  |/     /|
    \__     |    -   \  -    |     /#|
     \#\     |        |      |   /###|
      \##\   |       \|     |  /#####|
       \###\  |   _______  | /######|
        \####\ | / \/ \/ \|/#######|
        |######\|        |#########|
        |########\______/##########|
        |#########\    /##########/
        |##########\  |#########/\
        /###########\/########/###\
    /################\######/########\
   /##################\###/###########\
  /###################\#/##############\
 /####################/#################\
/###################/####################\
    
"""
WEREWOLF=r"""

                                     /\
                                ( ;`~v/~~~ ;._
                             ,/'"/^) ' < o\  '".~'\\\--,
                           ,/",/W  u '`. ~  >,._..,   )'
                          ,/'  w  ,U^v  ;//^)/')/^\;~)'
                       ,/"'/   W` ^v  W |;         )/'
                     ;''  |  v' v`" W }  \\
                    "    .'\    v  `v/^W,) '\)\.)\/)
                             `\   ,/,)'   ''')/^"-;'
                                  \
                                   '". _
                                        \
                                            
    """

def battle(enemy,img,p1):
        clear()   
        print(f"The {enemy.name} appeared!")
        sleep(1)
            
        print(img)
        while enemy.hp > 0 and p1.hp > 0:
                
            match p1.name:
                
                case "elf":
                    
                    clear()
                    print(img)
                    print(f"{enemy.name}: {enemy.hp} HP\n{p1.pname}: {p1.hp} HP\n")
                    choice = int(input("1: simple attack\n2: bow shot\n"))
                    if choice == 1:
                        p1.dmg(enemy)
                    elif choice == 2:
                        p1.bow_shot(enemy)
                    
                case "knight":
                    
                    clear()
                    print(img)
                    print(f"{enemy.name}: {enemy.hp} HP\n{p1.pname}: {p1.hp} HP\n")
                    choice = int(input("1: simple attack\n2: vertical slash\n"))
                    if choice == 1:
                        p1.dmg(enemy)
                    elif choice == 2:
                        p1.vertical_slash(enemy)
                    
                case "sorcerer":
                    
                    clear()
                    print(img)
                    print(f"{enemy.name}: {enemy.hp} HP\n\n{p1.pname}: {p1.hp} HP\n      {p1.mana} MANA\n")
                    choice = int(input("1: simple attack\n2: magic spell\n"))
                    if choice == 1:
                        p1.dmg(enemy)
                    elif choice == 2:
                        p1.spell(enemy)
                        
            if enemy.hp > 0:
                    
                match enemy.name:
                    case "werewolf":
                        choice = randint(0,100)
                        if choice <= 70:
                            enemy.dmg(p1)
                        elif choice > 70:
                            enemy.bite(p1)
                                
                    case "vampire":
                        choice = randint(0,100)
                        if choice <= 70:
                            enemy.dmg(p1)
                        elif choice > 70:
                            enemy.vampirism(p1)
                                
                    case "orc":
                        choice = randint(0,100)
                        if choice <= 70:
                            enemy.dmg(p1)
                        elif choice > 70:
                            enemy.fall(p1)
        if enemy.hp <= 0:
            p1.win(enemy)
        else:
            p1.lose()
        sleep(7)
        clear()