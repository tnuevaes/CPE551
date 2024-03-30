# Author: Teddy Nueva Espana
# Date: 3/26/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: The program houses a Warehouse class that contains information and functions regarding adding and removing from a number of items in storage

class Warehouse:
    def __init__(self, goods):
        self.__goods = goods #goods = int of goods
        
    def getGoods(self):
        return self.__goods
    
    def addGoods(self):
        self.__goods += int(input("How many goods would you like to add: "))
    
    def removeGoods(self):
        amount = int(input("How many goods would you like to remove: "))
        if (self.__goods - amount) < 0:
            # Not enough to remove
            print(f"Removing {amount} item/s from the warehouse removes more than the current amount in the warehouse!")
        else:
            self.__goods -= amount
            
        
    