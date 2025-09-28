#Program for Demonstrating the Garbage Collection
#DestEx3.py
import time
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterized Const: ")
		self.eno=eno
		self.ename=ename
		print("\tEmployee Number:{}".format(self.eno))
		print("\tEmployee Name:{}".format(self.ename))
		print("---------------------------------------------------------")
	def __del__(self):
		print("\tGC calls __del__() for De-allocating Memory space:")

#Main Program
print("Program Execution Started")
e1=Employee(10,"RS") # Object Creation Makes the PVM to Call Parameterized Const
print("\tNo  Longer Interested to use an Object e1")
time.sleep(5)
del e1 # Once we delete an object by using del operator, GC calls Its Own Destructor forcefully
time.sleep(5)
e2=Employee(20,"TR") # Object Creation Makes the PVM to Call Parameterized Const
print("\tNo  Longer Interested to use an Object e2")
time.sleep(5)
del e2 # Once we delete an object by using del operator, GC calls Its Own Destructor Forcefully
e3=Employee(30,"DR") # Object Creation Makes the PVM to Call Parameterized Const
print("\tNo  Longer Interested to use an Object e3")
time.sleep(5)
del e3 # Once we delete an object by using del operator, GC calls Its Own Destructor Forcefully
time.sleep(3)
print("Program Execution Ended")