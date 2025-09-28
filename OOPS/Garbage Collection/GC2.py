#Program for Demonstrating the Garbage Collection
#GCEX2.py
import sys,gc,time
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterized Const: ",id(self))
		self.eno=eno
		self.ename=ename
		print("\tEmployee Number:{}".format(self.eno))
		print("\tEmployee Name:{}".format(self.ename))
		print("---------------------------------------------------------")
	def __del__(self):
		global totmemspace
		print("\tGC calls __del__() for De-allocating Memory space:",id(self))
		totmemspace=totmemspace-sys.getsizeof(self)
		print("\tNOW TOTAL MEMORY SPACE=",totmemspace)

#Main Program
print("Program Execution Started")
print("\tInitially,Is GC Running: ",gc.isenabled()) # True
e1=Employee(10,"RS") # Object Creation Makes the PVM to Call Parameterized Const
e2=Employee(20,"TR") # Object Creation Makes the PVM to Call Parameterized Const
e3=Employee(30,"DR") # Object Creation Makes the PVM to Call Parameterized Const
totmemspace=sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
gc.disable()
print("\tNow,Is GC Running: ",gc.isenabled()) # False
print("\tTOTAL MEMORY SPACE In Main Program=",totmemspace)# 144
print("Program Execution Ended")
time.sleep(5)
#At the end of the Program execution Garbage Collector calls Its Own Destructor--Called Automatic Garbage Collection