from DivFunction import div
from DivException import MyDivException
#from Python.Exception.DivException import MyDivException

try:
    a=div(10,0)
except MyDivException:
    print("Den cannot be zero")
else:
    print("Program succesfull")
    print("The answer is {}".format(a))
