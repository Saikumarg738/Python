#Program for Demonstrating the Garbage Collection
#DestEx5.py
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
print("Program Execution Ended")
#At the end of the Program execution Garbage Collector calls Its Own Destructor--Called Automatic Garbage Collection