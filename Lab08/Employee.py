# Author: Teddy Nueva Espana
# Date: 4/2/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: 

class Employee:
    def __init__(self, name, id, rate):
        # Declare class variables
        self._name = name
        self._idNumber = id
        self._rate = rate

    
    def calcPay(self, hours):
        return self._rate * hours # Hours = int
    
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
        
    def getID(self):
        return self._idNumber
    
    def setID(self, newID):
        self._idNumber = newID
        
    def getRate(self):
        return self._rate
    
    def setRate(self, rate):
        self._rate = rate
    