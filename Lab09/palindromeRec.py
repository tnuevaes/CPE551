# Author: Teddy Nueva Espana
# Date: 4/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: Recursive Palindrome Test

def palinTest(string):
    length = len(string)
    if length <= 1:
        
    for i in range(len(string)):
        if string[i] != string[-i-1]:
            return False
    return True
        
def main():
    word = input("Enter word to test: ")
    print(palinTest(word),'The string is a palindrome')
main()