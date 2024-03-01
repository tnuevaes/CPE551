# Author: Teddy Nueva Espana
# Date: 3/1/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: Main function for converting data from file to symbols representing art 
# calling functions from pbnFunctions.py

import pbnFunctions

def main():
    filename = pbnFunctions.getFileName()
    pbnFunctions.processFile(filename)
    print("Image is located in the file: painting.txt")
main()