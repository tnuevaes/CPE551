# Author: Teddy Nueva Espana
# Date: 3/26/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program utilizes a product class to to prompt the user for and calculate the total cost of a certain amount of a given item at a set price

import Product

def calcTotal(product):
    """calcuate total cost of a product class object"""
    # units * price
    units = float(product.getUnits()) #Convert str to float
    price = product.getPrice()
    return units * price
    

def main():
    item = Product.Product()
    
    # Set name, units, and price
    item.setName(input("Enter Product name: "))
    item.setUnits(input("Enter Desired Amount: "))
    item.setPrice(9.99)
    
    # Call calcTotal function to calculate and set value in calc
    calc = calcTotal(item)
    
    # set total cost to item Cost
    item.setCost(calc)
    
    # print('The final cost for', format(item.getUnits()),'units of',item.getName(),'is: $',format(item.getCost(),'.2f'), 'at $',format(item.getPrice(),'.2f'),'per unit')
    print('Name: ',item.getName() )
    print('Units: ',format(item.getUnits()))
    print('Price: ','$'+format(item.getPrice(),'.2f'))
    print('Total Cost: ','$'+format(item.getCost(),'.2f'))
main()