# Author: Teddy Nueva Espana
# Date: 1/30/24
# Description: Given a duration of time, this program computes 
# the velocity, average velocity, and displacement of an object.

# Useful values:
acceleration = 5.25
initialVelocity = 8.25

# input time:
time = float(input("input time: "))

# Calculate the properties of the object:

#velocity
vel = initialVelocity + acceleration * time
#avg velocity
avgVel = initialVelocity + (acceleration * time)/2
#displacement
disp = initialVelocity * time + (acceleration * (time**2))/2

# Print the results:
print(f"time = {time}\n")
print(f"velocity \t = {vel}")
print(f"average velocity = {avgVel}")
print(f"displacement \t = {disp}")
