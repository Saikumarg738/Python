from Python.Exception.NameFunction import *

try:
    a=input("ENter name : ")
    na=checkname(a)
except ZeroLenght:
    print("You cannot print zero characters")
except EmptyName:
    print("Cannot give empty name")
except InvalidName:
    print("Name is invalid")
else:
    print("The name is {}".format(na))
