# Author: Teddy Nueva Espana
# Date: 3/26/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: his program contains a Product class that contains information and functions regarding an item's price, cost, name, and number of units
class Product:
    def __init__(self):
        # Declare class variables
        self.__name = "" 
        self.__units = 0
        self.__price = 0
        self.__cost = 0
    
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
        return f"The product cost is ${self.__cost} for {self.__units} units at a price of ${self.__price}"
 