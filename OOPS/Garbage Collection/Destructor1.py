#Program for Demonstrating the Garbage Collection
#DestEx1.py
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterized Const: ",id(self))
		self.eno=eno
		self.ename=ename
		print("\tEmployee Number:{}".format(self.eno))
		print("\tEmployee Name:{}".format(self.ename))
		print("---------------------------------------------------------")
	def __del__(self):
		print("\tGC calls __del__() for De-allocating Memory space:",id(self))

#Main Program
print("Program Execution Started")
e1=Employee(10,"RS") # Object Creation Makes the PVM to Call Parameterized Const
e2=Employee(20,"TR") # Object Creation Makes the PVM to Call Parameterized Const
e3=Employee(30,"DR") # Object Creation Makes the PVM to Call Parameterized Const
print("Program Execution Ended")
#At the end of the Program execution Garbage Collector calls Its Own Destructor--Called Automatic Garbage Col