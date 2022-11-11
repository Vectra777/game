from player.player import *
from ennemy.ennemy import *
from random import *
from time import sleep
from reprint import *
import sys

sys.path.insert(0,'global')

clear()
reprint("hello!!")
sleep(2)
reprint("Who are you?\n")
name=input("")
clear()
reprint(f"{name}? that's cringe...")
sleep(2)
reprint("anyway welcome.")