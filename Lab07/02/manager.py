# Author: Teddy Nueva Espana
# Date: 3/26/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program utilizes a Warehouse class to prompt the user on what to do with a given Warehouse class object

import Warehouse

def main():
    storage = Warehouse.Warehouse(0)
    
    choice = 0
    
    while choice != "4":
        choice = input(f"""
Welcome to the warehouse!
Enter choice of what you would like to do:
    1. Add Item to Warehouse
    2. Remove Item from Warehouse
    3. Output Total
    4. Quit
Choice: """)
        if choice == "1":
            # add item
            storage.addGoods()
        elif choice == "2":
            # Remove item
            storage.removeGoods()
        elif choice == "3":
            # Output total
            print(f"There are {storage.getGoods()} items in storage")
        elif choice == "4":
            # Quit
            print("Good Bye !")
            break
        else:    
            print("Not a valid choice")
        
main()
            
        