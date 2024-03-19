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


def main():
    
    info = loadFlower()
    testlist = [" ","b","c"]
    
    for element in testlist:
        if element == " " or element in info:
            print("True")
        else:
            raise TypeError(f"{element} is not a known flower type")
        
main()