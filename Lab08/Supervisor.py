# Author: Teddy Nueva Espana
# Date: 4/2/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program defines a Supervisor class that inherits from Employee class

from Employee import Employee

class Supervisor(Employee):
    def __init__(self, name, id, rate, level):
        super().__init__(name, id, rate)
        # Declare class variables
        self.__level = level
        self._idNumber = id
        self._rate = rate

    
    def calcPay(self, hours):
        base = super().calcPay(hours)
        bonus_total = base + (1000.00 * self.__level)
        return bonus_total
    
    def getLevel(self):
        return self.__level
    
    def setLevel(self, level):
        self.__level = level