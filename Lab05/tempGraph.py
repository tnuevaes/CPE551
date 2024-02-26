# Author: Teddy Nueva Espana
# Date: 2/23/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: Generates 12 random temperatures corresponding to 12 hours and plots the values
# using Matplotlib

import matplotlib.pyplot as plt
import random as rdm

time = [1,2,3,4,5,6,7,8,9,10,11,12]
cities = ["New York", "Chicago", "Los Angeles"]

#New York
ny = []
for i in range(12):
    ny.append(rdm.randint(10,30))
#Chicago
chi = []
for i in range(12):
    chi.append(rdm.randint(10,30))
#Los Angeles
la = []
for i in range(12):
    la.append(rdm.randint(10,30))

plt.plot(time,ny)
plt.plot(time,chi)
plt.plot(time,la)

plt.title("Hourly Temperatures")
plt.xlabel("Hours")
plt.ylabel("Temperature")
plt.legend(cities)
plt.show()