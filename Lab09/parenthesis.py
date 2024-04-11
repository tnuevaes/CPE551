# Author: Teddy Nueva Espana
# Date: 4/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: 

count = 0

def parenTest(line, pos):
    global count
    length = len(line)
    if pos == length: # base case
        return True
    
    if line[pos] == '(':
        count += 1
    elif line[pos] == ')':
        count -= 1
        if count < 0:
            return False
    return parenTest(line, pos + 1)

def main():
    test = input("Enter line of parentheses to test: ")
    result = parenTest(test,0)
    if result == False:
        print("Parentheses not balanced")
    else:
        print("Parentheses balanced")

main() 