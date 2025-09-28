import sys

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("The name is",self.name)
        print("The age is",self.age)
        print("Size is",sys.getsizeof(self))
    def __del__(self):
        global totmemspace
        spacecons=totmemspace-sys.getsizeof(self)
        print("Space consumed is",spacecons)

a=Employee("sai",27)
b=Employee("Kumar",26)
c=Employee("Gangu",25)
totmemspace=sys.getsizeof(a)+sys.getsizeof(b)+sys.getsizeof(c)