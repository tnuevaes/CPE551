# Author: Teddy Nueva Espana
# Date: 2/8/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program generates two random integers inclusively
# from 1-10 and 11-20 respectively and finds the sum of the 
# odd integers between the two.

import random

x = random.randint(1,10)
y = random.randint(11,20)
start = 0
end = 0


if x % 2 == 0 :
    start = x + 1
else :
    start = x

if y % 2 == 0 :
    end = y - 1
else :
    end = y

sum = 0

for i in range(start,end+1,2) :
    sum += i

print(f"The randomly generated range of values is {x,y}") 
print(f"The sum of odd integers within the range {x,y} is: {sum}")
    

