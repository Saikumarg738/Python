from AddEmployee import *
from DeleteEmployee import *
from DisplayAllEmployee import *


print("*************Welcome to Employee Data****************")
print("Please select following option")

print("To Add employee, enter 1")
print("To delete employee, enter 2")
print("To update employee, enter 3")
print("To view employee, enter 4")
print("To view all employee, enter 5")

option=int(input("Enter your option : "))

match(option):
    case 1:
        empadd()
    case 2:
        empdel()
    case 3:
        EmpUpdate()
    case 4:
        displayall()
    case 5:
        ViewAll
    case _:
        print("Please enter from the option specified")
