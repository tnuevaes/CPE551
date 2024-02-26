# Author: Teddy Nueva Espana
# Date: 2/23/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program allows a user to perform various fuctions regrading a 
# list of laboratory equipment

LabEquip = []

choice = 0

while choice != 4:
    print("\nWelcome to the inventory manager for your laboratory")
    print("You can choose from the following options: "
          "\n 1. Add Equipment"
          "\n 2. Remove Equipment"
          "\n 3. Display Current Equipment"
          "\n 4. Leave the Laboratory Manager")
    choice = float(input("What would you like to do: "))

    if choice == 1:
        if len(LabEquip) < 5:
            LabEquip.append(input("What would you like to add: "))
        else:
            print("Cannot add any more equipment!")
    elif choice == 2:
        if len(LabEquip) == 0:
            print("Nothing to remove")
        else:
            remove_item = input("What would you like to remove: ")
            if remove_item in LabEquip:
                LabEquip.remove()
            else:
                print("item not in list")
    elif choice == 3:
        display = ", ".join(map(str, LabEquip))
        print(f"The laboratory currently contains: {display}" )
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Not a valid input, please try again\n")

