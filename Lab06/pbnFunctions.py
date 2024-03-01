# Author: Teddy Nueva Espana
# Date: 3/1/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: Functions for converting data from file to symbols representing art

import os

def getFileName():
    """_summary_
        Prompts user for file name to store or notify if file does not exist
    Returns:
        String : fileName
    """
    fileName = input("Please input file you wish to have painted:")
    while os.path.exists(fileName) == False:
        if os.path.exists(fileName) == False:
            print(f"{fileName} does not exist")
            fileName = input("Please input file you wish to have painted:")
        else:
            break
    return fileName

def convertLine(line):
    """Converts a line in a file from text to representative symbols

    Args:
        line String : line within a file that needs to be converted from numbers to symbols

    Returns:
        newLing String : line composed of corresponding symbols
    """
    line = line.strip()
    #Convert to list
    lineList = line.split(",")
    newLine = ""
    #create new string from list 
    for x in range(len(lineList)):
        if lineList[x] == '1':
            newLine += " "
        elif lineList[x] == '2':
            newLine += ","
        elif lineList[x] == '3':
            newLine += "_"
        elif lineList[x] == '4':
            newLine += "("
        elif lineList[x] == '5':
            newLine += "O"
        elif lineList[x] == '6':
            newLine += ")"
        elif lineList[x] == '7':
            newLine += "-"
        elif lineList[x] == '8':
            newLine += '"'
    return newLine
    
def processFile(filename):
    """Opens input file for reading and creates file to write final output
        Iterates through input file and calls convertLine() for writing to the output

    Args:
        filename string : file name within the current directory
    """
    inputFile = open(filename,"r")
    outputFile = open("painting.txt","w")
    for line in inputFile:
        newLine = convertLine(line)
        outputFile.write(newLine + "\n")
    inputFile.close()
    outputFile.close()
        
        
    