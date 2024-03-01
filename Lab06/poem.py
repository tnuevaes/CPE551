# Author: Teddy Nueva Espana
# Date: 3/1/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: Prompts user to input text file containing a poem,
# summarizes the poem in a new file containing the title, author, and brief summary

import os

def main():
    existCheck = False
    
    while existCheck == False:
        filename = input("Please input the name of the poem you wish summarized: ")
        existCheck = os.path.exists(filename)
        if existCheck == False:
            print(f"{filename} does not exist")
        else:
            break
    
    poem = []
    #open file
    poemFile = open(filename, "r")
    # read through file, append to list with lines of poem
    for line in poemFile:
        poem.append(line)
        
    # set variables for parts of poem
    title = poem[0]
    author = poem[1]
    line1 = poem[2]
    line2 = poem[3]
    line3 = poem[4]
    
    poemFile.readline()
    for line in poemFile:
        print(line.strip())
        
    
    output = open("Output.txt",'w')
    output.write(f"The name of the poem is {title}")
    output.write(f"the author of the poem is {author}")
    output.write(f"A preview of the poem is:\n")
    output.write(f"{line1}{line2}{line3}")
    
    
        
    
main()
        