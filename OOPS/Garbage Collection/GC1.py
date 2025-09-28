#GCEX1.py
import gc
print("Program Execution Started")
print("\tInitially,Is GC Running: ",gc.isenabled()) # True
a=10
b=20
c=a+b
gc.disable()
print("\tVal of a=",a)
print("\tNow, Is GC Running: ",gc.isenabled()) # False
gc.enable()
print("\tVal of b=",b)
print("\tSum=",c)
print("\tNow, Is GC Running: ",gc.isenabled()) # True
print("Program Execution Ended")