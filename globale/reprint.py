from os import system
import platform
_last_print_len = 0 
def reprint(msg, finish=False): 
    global _last_print_len 
         
    print(' '*_last_print_len, end='\r') 
         
    if finish: 
        end = '\n' 
        _last_print_len = 0 
    else: 
        end = '\r' 
        _last_print_len = len(msg) 
         
        print(msg, end=end) 

def clear():
    if platform.system() == "Windows":
        system('cls')
    else:
        system('clear')