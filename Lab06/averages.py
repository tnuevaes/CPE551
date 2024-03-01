# Author: Teddy Nueva Espana
# Date: 3/1/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: Reads through a file storing numbers on separate lines, outputs
# the numbers and calculates the average of the numbers

def main():
    # Create empty list to store number data
    numberList = []
    # Open file, numbers.txt file must be in same directory as averages.py
    file = open('numbers.txt', "r")
    
    
    # Read through file and add each line to the list
    for line in file:
        numberList.append(line)
        print(line.strip())
    #Compute Average
    sum = 0
    for x in range(len(numberList)):
        # calculate sum within loop while converting each item in list to int
        sum += int(numberList[x])
    avg = sum / len(numberList)
    
    file.close()
    print(f"The average of the numbers is: {avg}")
main()