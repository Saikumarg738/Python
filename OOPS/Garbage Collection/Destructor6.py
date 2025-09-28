#Program for Demonstrating the Garbage Collection
#DestEx6.py
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
e2=e1 # Deep Copy
e3=e1 # Deep Copy
print("\tNo  Longer Interested to use an Object e1")
time.sleep(5)
e1=None # Once we Make  an object Ref as None , GC will not call Its Own Destructor forcefully bcoz still e2 and e3 points to an object
time.sleep(5)
print("\tNo  Longer Interested to use an Object e2")
time.sleep(5)
e2=None # Once we Make  an object Ref as None , GC will not call Its Own Destructor forcefully bcoz still e3 points to an object
print("\tNo  Longer Interested to use an Object e3")
time.sleep(5)
e3=None # Once we Make  an object Ref as None , GC calls Its Own Destructor Forcefully bcoz No Object Points  to memory space.
time.sleep(3)
print("Program Execution Ended")