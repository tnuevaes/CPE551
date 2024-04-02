# Author: Teddy Nueva Espana
# Date: 4/2/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: 

from Worker import Worker
from Supervisor import Supervisor

def calcTotalPay(Employee_List):
    sumTotal = 0
    for employee in Employee_List:
        sumTotal += employee.calcPay(40)    
    return sumTotal

def listEmployees(Employee_List):
    print("====== Employee List ======")
    
    for person in Employee_List:
        if isinstance(person, Supervisor): 
            print(f"""
name: {person.getName()}
ID: {person.getID()}
Rate: ${format(person.getRate(),'.2f')}
Level: {person.getLevel()}""")
                    
        elif isinstance(person, Worker):
            print(f"""
name: {person.getName()}
ID: {person.getID()}
Rate: ${format(person.getRate(),'.2f')}
Shift: {person.getShift()}""")
        
def main():
    Employee_List = []
    
    amount = int(input("How many employees would you wish to add: "))
    i = 0
    while i < amount:
        choice = input("""
Add a:
    1. Supervisor
    2. Worker
    Choice: """)
        if choice == "1":
            # Add supervisor
            name = input("Enter name: ")
            newID = int(input("Enter ID number: "))
            rate = float(input("Enter rate: "))
            level = int(input("Enter Level: "))
            newEmployee = Supervisor(name, newID, rate, level)
            Employee_List.append(newEmployee)
            i+=1
        elif choice == "2":
            # Add worker
            name = input("Enter name: ")
            newID = int(input("Enter ID number: "))
            rate = float(input("Enter rate: "))
            shift = int(input("Enter Shift (1 for day, 2 for night): "))
            newEmployee = Worker(name, newID, rate, shift)
            Employee_List.append(newEmployee)
            i+=1
        else:
            print("Not a valid choice, try again")
            
    
    listEmployees(Employee_List)
    print("The total cost of all of the worker's pay is $"+format(calcTotalPay(Employee_List),'.2f'))

main()