# Author: Teddy Nueva Espana
# Date: 2/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program generates a random integer within the range of 0 to 450 representing the distance hit by the batter
# and tells the outcome of the batter's hit based on the range of values that the random integer is in.

import random
n = 1
while(n == 1):
    bat = input("type 'y' to bat!")
    if bat == "y" : 
        distance = random.randint(0,450)
        if distance > 400 :
            print(f"Distance = {distance}, It's a home run! The batter scores a run for the team!")
        elif 135 <= distance <= 400 :
            print(f"Distance = {distance}, The ball is in the outfield! Batter goes to third base!")
        elif 10 <= distance <= 134 :
            print(f"Distance = {distance}, The ball is in the infield! Batter goes to first base!")
        elif 1 <= distance <= 9 :
            print(f"Distance = {distance}, Batter bunted the ball! They go to first base!")
        elif distance == 0 :
            print(f"Distance = {distance}, STRIKE!")
    else :
        n = 0
