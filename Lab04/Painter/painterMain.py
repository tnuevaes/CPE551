# Author: Teddy Nueva Espana
# Date: 2/16/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program prompts the user for a choice of art to 
# display as well as a symbol to be used as a border around the art

import painterFuncs

def main():
    art, border = painterFuncs.intro()
    if art == "1":
        painterFuncs.sleepingCat(border)
    elif art == "2":
        painterFuncs.sailingShip(border)
    elif art == "3":
        painterFuncs.snail(border)
    elif art == "4":
        painterFuncs.dog(border)
    else:
        painterFuncs.blank(border)
        print("We do not seem to have that painting")
        exit(-1)
    print("I hope you enjoy the art!")        
    
main()
