# Author: Teddy Nueva Espana
# Date: 4/19/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program uses the Stack class to read through a list and produce a stack 

from Stack import Stack, EmptyStackException

def main():
    stack = Stack()
    inputFile = open("inputStack.txt","r")
    
    for line in inputFile:
        split = line.strip().split()
        action = split[0]
        if len(split) > 1:
            number = split[1]
        else: number = None
        
        if action == "push":
            stack.push(number)
            print(f"pushed {number}")
        elif action == "pop":
            try:
                print(f"popped {stack.pop()}")    
            except Exception:
                print("Nothing to pop")
        elif action == "peek":
            try:
                print(f"peeked at {stack.peek()}")
            except:
                print("Nothing to peek")
        elif action == "clear":
            stack.clear()
            print("Clearing the stack")
        elif action == "print":
            print(stack)
    
main()
        
    