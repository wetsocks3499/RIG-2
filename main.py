#########
import splash
from compo import *
import random
from colorama import Style, Fore
#########
print(Style.RESET_ALL)
name = input("Before we begin, what's your name?\n>>> ")
print("\nHello, "+name+"!\n")
def insult():
    adjPrint = random.choice(adj)
    nounPrint = random.choice(noun)
    verbPrint = random.choice(verb)
    specialPrint = "" # storage value

    if random.random(1, 100) == 15: # 15% chance
        specialPrint = random.choice(special)

    print(name+", you're a"+Fore.RED+specialPrint+adjPrint+nounPrint+verbPrint+"!")  # ugly, but it works.
    specialPrint = "" # resets the variable
    retry = "y"
    print(Style.RESET_ALL)
    retry = input("\nWould you like to hear another one? (y/n)\n")
    if retry == "y":
        retry = ""
        insult()
    elif retry == "n":
        print("\nGoodbye.")
        exit()
    




## run call
insult()