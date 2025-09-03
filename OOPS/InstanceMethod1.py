class Student:
    def readstudent(self,number):
        print("Enter data of student number {}".format(number))
        self.name=input("Enter name : ")
        self.id=int(input("Enter ID : "))

    def displaystudent(sai,number):
        print("Displaying data of student number {}".format(number))
        print("Student {} name is {}".format(number,sai.name))
        print("Student {} id is {}".format(number, sai.id))

s1=Student()
s2=Student()

print("Data of s1 is ",s1.__dict__)
print("Data of s2 is ",s2.__dict__)

s1.readstudent(1)
s2.readstudent(2)

print("Data of s1 is ",s1.__dict__)
print("Data of s1 is ",s2.__dict__)

s1.displaystudent(1)
s2.displaystudent(2)

