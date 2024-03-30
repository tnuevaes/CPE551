# Author: Teddy Nueva Espana
# Date: 3/26/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program contains a SmartProduct class that contains information and functions regarding an item's price, cost, name, number of units, and ID

class SmartProduct:
    def __init__(self, newID, name, units, price ):
        self.__id = newID
        self.__name = name
        self.__units = units
        self.__price = price
        self.__cost = price * units
    
    def getID(self):
        return self.__id
    
    def setID(self, newID):
        self.__id = newID
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
        
    def getUnits(self):
        return self.__units
    
    def setUnits(self, units):
        self.__units = units
        
    def getPrice(self):
        return self.__price
    
    def setPrice(self, price):
        self.__price = price
    
    def getCost(self):
        return self.__cost
    
    def setCost(self, cost):
        self.__cost = cost
        
    def __str__(self):
        return f"The product cost is: {self.__cost} units: {self.__units} price: {self.__price}"
 