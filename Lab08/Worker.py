# Author: Teddy Nueva Espana
# Date: 4/2/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program defines a Worker class that inherits from Employee class

from Employee import Employee

class Worker(Employee): 
    def __init__(self, name, id, rate, shift):
        super().__init__(name, id, rate)
        self.__shift = shift # 1 = day shift, 2 = night shift
        
    def getShift(self):
        if self.__shift == 1:
            return "Day Shift"
        elif self.__shift == 2:
            return "Night Shift"
    
    def setName(self, shift):
        self.__shift = shift
        
