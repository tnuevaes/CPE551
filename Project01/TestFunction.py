import os 

def loadFlower():
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
        line = line.strip()
        lineList = line.split(",")  #[0] = Flower letter, [1] = flower name, [2] = pollen value
        info[lineList[0]] = (lineList[1],lineList[2])
    inputFile.close
    return info
    
def createField(info):  #info -> dictionary of Tuples with flower info from loadFlower()
    # create field
    # return 2d list
    
    fileName = input("Enter name of file containing the field:  ") #CSV format
    while not os.path.exists(fileName):
        if os.path.exists(fileName) == False:
            print(f"{fileName} does not exist")
            fileName = input("Enter name of file containing the field: ")
        else:
            break
    
    grid = []
    
    inputFile = open(fileName,"r")
    for line in inputFile:
        line = line.strip()
        lineList = line.split(",")
#        for element in lineList:
#           if element == " " or element in info:
#               continue
#           else:
#              raise TypeError(f"{element} is not a known flower type")
        grid.append(lineList)
    return grid


def printField(field):
    # Print out 2d list in grid format with index numbers along top and left
   
   print("The map is as follows:")
   print('   ', end='')
   for i in range(len(field)):
       print(f'{i:<4}', end='')
   print()

   for i,row in enumerate(field):
        print(format(i,'<1'),'|', end='')
        for element in row:
            print(format(element, '1'), '|', end=' ')
        print()

def copyField(field):
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

def main():
    field = createField(loadFlower())
    printField(field)
    printField(copyField(field))
main()