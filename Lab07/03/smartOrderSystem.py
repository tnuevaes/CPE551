# Author: Teddy Nueva Espana
# Date: 3/26/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program utilizes a SmartProduct class to prompt the user for and calculate the total cost of a multiple items at set prices

import SmartProduct

def calcTotal(productList):
    """calcuate total cost of a list of product class object"""
    sumTotal = 0
    for product in productList:
        sumTotal += product.getCost()    
    return sumTotal
    

def main():
    
    items = []
    amount = int(input("How many products would you like to order: "))
    
    for i in range(amount):
        name = input("Enter item name: ")
        units = int(input("Enter number of units: "))
        newItem = SmartProduct.SmartProduct(i+1, name, units, 9.99)
        items.append(newItem)
    
    
    print("You Ordered:")
    
    for item in items:
        print('Product ID:', format(item.getID()))
        print('Product Name: ',item.getName())
        print('Price: $'+format(item.getPrice(),'.2f'))
        print('Total Cost: $'+format(item.getCost(),'.2f'))    

    Total = calcTotal(items)

    print("The total cost of your order is: $"+ format(Total,'.2f'))




    """
    # Set name, units, and price
    item.setName(input("Enter Product name: "))
    item.setUnits(input("Enter Desired Amount: "))
    item.setPrice(9.99)
    
    # Call calcTotal function to calculate and set value in calc
    calc = calcTotal(item)
    
    # set total cost to item Cost
    item.setCost(calc)
    
    print('The final cost for', format(item.getUnits()),'units of',item.getName(),'is: $',format(item.getCost(),'.2f'), 'at $',format(item.getPrice(),'.2f'),'per unit')
    """
main()