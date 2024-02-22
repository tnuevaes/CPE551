# Author: Teddy Nueva Espana
# Date: 2/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program converts a user specified 
# number in the range of 1-9, inclusively, into the 
# equivalent Roman numeral


while(1):
    userNumber = input("Please enter a number between 1 and 9 to convert to a roman numeral:")
    if userNumber == "1" :
        print("The roman numeral is: \u2160" ) 
    elif userNumber == "2" :
        print("The roman numeral is: \u2161" )
    elif userNumber == "3" :
        print("The roman numeral is: \u2162" ) 
    elif userNumber == "4" :
        print("The roman numeral is: \u2163" ) 
    elif userNumber == "5" :
        print("The roman numeral is: \u2164" ) 
    elif userNumber == "6" :
        print("The roman numeral is: \u2165" ) 
    elif userNumber == "7" :
        print("The roman numeral is: \u2166" ) 
    elif userNumber == "8" :
        print("The roman numeral is: \u2167") 
# using \u2167 within the print statement for the number '8' prints out VII instead of
# VIII in my terminal, which is why I am including a second print statement using literal string 'VIII'
# If the program is able to print VIII properly for the input of 8, ignore the second print statement
        print("The roman numeral is: VIII") 
    elif userNumber == "9" :
        print("The roman numeral is: \u2168" )
    else :
        print("Number out of range")
        break
        
