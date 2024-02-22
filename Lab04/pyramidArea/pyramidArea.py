# Author: Your name
# Date: Today's date
# Description: This program prompts the user for side and height information of a 
# square pyramid and computes the base area, side area, and total surface area.

# function definitions
def calcBaseArea(side):
    return side ** 2

# add your function definition for calcSideArea here

def calcSideArea(side, height):
    return 2 * side * (((side**2 / 4)+(height**2))**0.5) 

# add your function definition for prntSurfArea here
def prntSurfArea(base, side):
    print(f"The total surface area of the square pyramid is {base + side} square feet")

def main():
    side = float(input("Enter the side length of the base of the square pyramid in feet: "))

    height = float(input("Enter the height of the square pyramid in feet: "))

    base_area = calcBaseArea(side)
    print(f"Base surface area of the square pyramid is {base_area} square feet.")

    # add your function to calculate the side area and assign
    side_area = calcSideArea(side, height)
    # the result to side_area, then print the result
    print(f"Side surface area of the square pyramid is {side_area} square feet.")

    # add your function call to print the total surface area
    prntSurfArea(base_area, side_area)
main()