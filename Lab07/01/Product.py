# Author: Teddy Nueva Espana
# Date: 3/26/24
# I pledge my honor that I have abided by the Stevens honor system
# Description:

class Product:
    def __init__(self):
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
        
    def getprice(self):
        return self.__price
    
    def setprice(self, price):
        self.__price = price
    
    def getCost(self):
        return self.__cost
    
    def setCost(self, cost):
        self.__name = cost