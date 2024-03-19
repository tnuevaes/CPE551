# Author: Teddy Nueva Espana
# Date: 3/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: Project 1


import BeeFunctions as bf

def main():
    info = bf.loadFlower()
    try:
        hiddenField = bf.createField(info)
    except TypeError as err:
        print(err)
        exit(-1)
    visibleField = bf.copyField(hiddenField)
    
    scouts = 5
    workers = 5
    curr_pollen = 0
    POLLEN_TO_WIN = 20
    bf.gameIntro(info, scouts, workers, POLLEN_TO_WIN)
    
    while curr_pollen < POLLEN_TO_WIN and scouts + workers != 0:
        #GAME START
        print(f"You currently have {scouts} scout bees and {workers} worker bees left")
        print(f"You currently have {curr_pollen} units of pollen harvested")
        print(f"On the grid, 'H' represents the starting hive")
        bf.printField(visibleField)
        choice = input("Which type of bee would you like to send out(S: Scout, W: Worker): ")
        if choice == "s": #Scout chosen
            if scouts > 0:
                x = input("Enter x coordinate: ")
                y = input("Enter y coordinate: ")
                scouts -= 1
                bf.checkSentPosition(hiddenField, visibleField, x, y, choice, info) 
            else:
                print("Out of scout bees")
        elif choice == "w": #Worker chosen
            if workers > 0:
                x = input("Enter x coordinate: ")
                y = input("Enter y coordinate: ")
                workers -= 1
                curr_pollen += bf.checkSentPosition(hiddenField, visibleField, x, y, choice, info) 
            else:
                print("Out of worker bees")
        else:
            print("That is not a valid bee type")

    if curr_pollen > POLLEN_TO_WIN:
        print("You have won the game! you collected enough pollen for the hive.")
    elif curr_pollen < POLLEN_TO_WIN:
        print("You have lost the game. You have run out of bees and have not collected enough pollen.")

main()
        
        
        
    