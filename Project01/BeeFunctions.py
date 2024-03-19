# Author: Teddy Nueva Espana
# Date: 3/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: Project 1


import os 

def loadFlower():
    """loads in the file with flower info to use (dictionary)
    """
    # Load flower list
    info = {}
    fileName = input("Enter name of file containing the flower:pollen information: ") #CSV format
    while not os.path.exists(fileName):
        if os.path.exists(fileName) == False:
            print(f"{fileName} does not exist")
            fileName = input("Enter name of file containing the flower:pollen information: ")
        else:
            break
    
    inputFile = open(fileName, "r")
    for line in inputFile:
        line.strip()
        lineList = line.split(",")  #[0] = Flower letter, [1] = flower name, [2] = pollen value
        info[lineList[0]] = (lineList[1],lineList[2])
    inputFile.close
    return info
    
def createField(info):  #info -> dictionary of Tuples with flower info from loadFlower()
    # create field
    # return 2d list
    """creates field as a grid using lines from file input as rows

        takes in a dictionary of typles
    """
    
    fileName = input("Enter name of file containing the field: ") #CSV format # check existence
    while not os.path.exists(fileName):
        if os.path.exists(fileName) == False:
            print(f"{fileName} does not exist")
            fileName = input("Enter name of file containing the field: ")
        else:
            break
    
    grid = [] #Create grid to return
    
    inputFile = open(fileName,"r")
    for line in inputFile:
        line = line.strip() # Strip whitespace
        lineList = line.split(",") # Create list with each item being the strings in the line separated by commas
           # If element in list is not space, in the dictionary, or a P(Pitcher), or a H(Hive), raise TypeError
           # For some reason, statement is raising error when " " is found, next 3 lines are the problem, commented out for functionality
#        for x in range(len(lineList)):
#           if not (lineList[x].isspace() or lineList[x] in info or lineList[x] == "P" or lineList[x] == "H"): 
#               raise TypeError(f"{lineList[x]} is not a known flower type") 
        grid.append(lineList)
    return grid

def copyField(field):
    """Creates a copy of a field that only displays the hive location
        all other items are replaced by spaces
    """
    # create copy of the field
    # Flowers and Pitcher plants are spaces
    # Spaces are spaces
    # H is in same position
    EmptyField = []
    for y in range(len(field)): # rows
        row = []
        for x in range(len(field[0])): # cols
            if field[y][x] == "H" or field[y][x] == " ":
                row.append(field[y][x])
            else:
                row.append(" ")
        EmptyField.append(row)
    return EmptyField

def printField(field):
   """Takes in field, prints the field in pleasing grid format
    """
    # Print out 2d list in grid format with index numbers along top and left
   print("The map is as follows:")
   print('   ', end='')
   for i in range(len(field[0])):
       print(f'{i:<4}', end='') # print index numbers on top
   print()

   for i,row in enumerate(field): # enumerate() displays each line with the iteration number starting
        print(format(i,'<1'),'|', end='')
        for element in row:
            print(format(element, '1'), '|', end=' ')
        print()

def gameIntro(info, scouts, workers, pollen):
    """takes in dictionary of flower info, number of scouts, workers, and pollen to win
        displays game information
    """
    # takes in dictiory of tuples with info
        # Flower info
        # # of scout bees
        # # of worker bees
        # amount of pollen needed to win
    # Prints out rules of the game
    
    
    
    print(f"Welcome to Bee!\n"
          "In this game, you play as the queen bee trying to " 
          "produce honey from the pollen of flowers.\n"
          "You have two kinds of bees: scouts and workers \n"
          "Scouts fly to a location and reveal flowers in a 3x3 grid centered on that location.\n"
          "Workers fly to a location, reveal the flowers in a 3x3 grid centered on that location, and harvest pollen from any unharvested flowers\n"
          )
    print(f"you only have {scouts} scout bees and {workers} worker bees to harvest {pollen} units of pollen")
    print("A bee can only be sent out once, and a flower can only be harvested once")
    print("However, be careful of pitcher plants as they will trap a bee and prevent it from returning to the hive.")
    print("These are the flowers that are available to be harvested in this map:")
    for key,items in info.items():
        print(f"{key}: {items[0]}, {items[1]} units of pollen")

    
    return

def checkSentPosition(hidden, visible, x, y, bee, info):
   """takes in two fields, coordinate info, bee info, and flower data
        checks the coordinate and 3x3 grid for info regarding flowers and updates the visible grid
   
   """ 
   # Take in 2d hidden list, 2d visible list, x, y
   # pollen = # amount of pollen harvested
   x = int(x)
   y = int(y)
   pollen = 0
   # Check if coord is in bounds
   if x > len(visible[0]): 
       print("Bee has gone out of bounds")
       pollen = 0
   elif y > len(visible):
       print("Bee has gone out of bounds")
       pollen = 0 
   elif x < 0:
       print("Bee has gone out of bounds")
       pollen = 0
   elif y < 0:
       print("Bee has gone out of bounds")
       pollen = 0
   else:
        # examine 3x3 grid around x,y
        # Points around x,y are: 
        # (x-1,y-1), (x,y-1), (X+1,y-1)
        # (x-1,y) , (x,y) ,  (x+1,y)
        # (x-1,y+1), (x,y+1), (x+1,y+1)
        
        # max() to ensure that values passed into for loop are not out of list index range
        # smaller value chosen,
        firstRow = max(0,y-1) #
        lastRow = min(len(visible[0]),y+1) 
        firstCol = max(0,x-1)
        lastCol = min(len(visible),x+1)
        
        
        plant = 0
        #check for pitcher plant
        for i in range(firstRow, min(len(visible),(lastRow + 1))): # min() tests to see if the 3x3 grid would be out of bounds and uses the maximum value of grid instead of an out of bounds coordinate
                for j in range(firstCol, min(len(visible[0]),(lastCol + 1))):
                    if hidden[i][j] == "P":
                        print("The bee has encountered a pitcher plant! The bee did not return to the hive")
                        plant = 1
        if plant != 1:                
            if bee == "s":        
                # iterate through and replace with hidden list, bee finds plants:
                for i in range(firstRow, min(len(visible),(lastRow + 1))):
                    for j in range(firstCol, min(len(visible[0]),(lastCol + 1))):
                        visible[i][j] = hidden[i][j]
                
            elif bee == "w":
                # iterate through and replace with U 
                for i in range(firstRow, min(len(visible),(lastRow + 1))):
                    for j in range(firstCol, min(len(visible[0]),(lastCol + 1))):
                        if hidden[i][j] in info:
                            pollen += int(info[hidden[i][j]][1])
                            visible[i][j] = "U"
                        else:
                            visible[i][j] = hidden[i][j]
   return pollen

