import os

def getFileName(fileName):
    fileName = input("Please input file you wish to have read:")
    while os.path.exists(fileName) == False:
        if os.path.exists(fileName) == False:
            print(f"{fileName} does not exist")
            fileName = input("Please input file you wish to have read:")
        else:
            break
    return fileName
        
def readLine(line):
    line = line.strip()
    lineList = line.split(" ")
    return lineList # returns list of each item in an index
    
        
def writeGrid(fileName):
    inputFile = open(fileName,"r")
    size = 8
    grid = [[0 for i in range(size)] for h in range (size)] # [y][x]
            
    for line in inputFile:
        tempLine = readLine(line) #tempLine = LIST of LINE ELEMENTS
        for element in tempLine:
            grid[line][element] = tempLine[element]
    
    print(grid)
            
    inputFile.close()
    
    