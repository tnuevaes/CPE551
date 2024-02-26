# Author: Teddy Nueva Espana
# Date: 2/23/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program allows the user to input various distances into a list
# and the program records the trial # and value of the top 3 distances input

top_distances = [0,0,0]
top_trials = [0,0,0]

add = "y"
curr_trial = 1

while add == "y" :
    
    distance = int(input(f"Enter Distance for trial {curr_trial}:"))
    distances = []
    
    if distance > top_distances[0]:
        # top_distances.insert(0, distance)
        top_distances[2] = top_distances[1]
        top_distances[1] = top_distances[0]
        top_distances[0] = distance
        
        # top_trials.insert(0, curr_trial)
        top_trials[2] = top_trials[1]
        top_trials[1] = top_trials[0]
        top_trials[0] = curr_trial
        
    elif  top_distances[1] < distance < top_distances[0]:
        # top_distances.insert(1, distance)
        
        top_distances[2] = top_distances[1]
        top_distances[1] = distance

        # Add to top trials list
        # top_trials.insert(1, curr_trial)
        top_trials[2] = top_trials[1]
        top_trials[1] = curr_trial
        
    elif top_distances[2] < distance < top_distances[1]:
        # top_distances.insert(2, distance)
        
        top_distances[2] = distance
        
        # top_trials.insert(2, curr_trial)
        
        top_trials[2] = curr_trial
        
    add = input("Do you wish to enter another trial? (Y/N): ")
    curr_trial += 1
    
print("Now displaying top 3 distances:")

print("Trial   Distance")
print(format(top_trials[0],'>5d'),format(top_distances[0],'>10d'))
print(format(top_trials[1],'>5d'),format(top_distances[1],'>10d'))
print(format(top_trials[2],'>5d'),format(top_distances[2],'>10d'))


        