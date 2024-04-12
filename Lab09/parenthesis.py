# Author: Teddy Nueva Espana
# Date: 4/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: test if input parentheses are balanced

count = 0

def parenTest(line, pos):
    global count
    print(count)
    length = len(line)
    if pos == length: # base case -> must have same number of ) as ( by the end of string
        if count % 2 != 0: # uneven number of ( and )
            return False 
        else:
            return True # even number of ( and ) -> end of the string
    if line[pos] == '(': #Start count for parentheses
        count += 1  
    elif line[pos] == ')': #Reduce count for parentheses
        count -= 1
        if count < 0:
            return False
    return parenTest(line, pos + 1) # increase position in string, recursive test

def main():
    test = input("Enter line of parentheses to test: ")
    result = parenTest(test,0)
    if result == False:
        print("Parentheses not balanced")
    else:
        print("Parentheses balanced")

main() 