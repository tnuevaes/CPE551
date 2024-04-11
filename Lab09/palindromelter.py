# Author: Teddy Nueva Espana
# Date: 4/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: Test Palindrome using loops

def palinTest(string):
    for i in range(len(string)): # iterate through length of string
        if string[i] != string[-i-1]: # test if char at string index is equal to char at negative string index
            return False
    return True
        
def main():
    word = input("Enter word to test: ")
    result = palinTest(word)
    if result == False:
        print('The string is not a palindrome')
    else:
        print('The string is a palindrome')
main()