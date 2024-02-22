# Author: Teddy Nueva Espana
# Date: 2/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program simulates a position guessing game that provides 3 guesses to the user to guess and 
# learn where there position guess is in relation to the actual position coordinates.
guesses = 3
x_coord = 7
y_coord = 4

while(guesses != 0) :
    print(f"you have ({guesses}) guesses to find the coordinate!")
    x_guess = int(input(f"Enter 'x' guess: "))
    y_guess = int(input(f"Enter 'y' guess: "))
    if  1 > x_guess or y_guess > 10 :
        print("Guess is out of bounds")
    elif x_guess == x_coord and y_guess == y_coord:
        print(f"You guessed correctly, the position was ({x_coord},{y_coord})")
        break
    else :
        if x_guess > x_coord :
            print("Your guessed 'x' position is greater than the correct 'x' position")
        if x_guess < x_coord :
            print("Your guessed 'x' position is less than the correct 'x' position")
        if y_guess > y_coord :
            print("Your guessed 'y' position is greater than the correct 'y' position")
        if y_guess < y_coord :
            print("Your guessed 'y' position is less than the correct 'y' position")
        guesses -= 1  
if guesses == 0 :
    print(f"Out of guesses, You lose, and the correct position was: ({x_coord},{y_coord})")
    