# Author: Teddy Nueva Espana
# Date: 4/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: Recursive Palindrome Test

def palinTest(string):
    length = len(string)
    if length <= 1: #base case 
        return True
    elif string[0] != string[-1]: # Compare beginning of string to end
        return False
    
    return palinTest(string[1:-1]) # run recursive fuction with shortened string
        
def main():
    word = input("Enter word to test: ")
    result = palinTest(word)
    if result == False:
        print(f'{word} is not a palindrome')
    else:
        print(f'{word} is a palindrome')
main()