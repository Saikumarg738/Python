class Student:
    def __init__(sai,name,age):
        sai.name=name
        sai.age=age

    def display(self):
        print(self.name)
        print(self.age)

s1=Student("Sai",27)
s1.display()