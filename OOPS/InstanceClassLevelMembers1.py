class student:
    course="PYTHON"
s1=student()
s2=student()
print(type(s1))
print(type(s2))
print(type(student))
print("The object of S1 before are: ",s1.__dict__)
print("The object of S2 before are : ",s1.__dict__)
s1.name="Sai"
s1.no=331459
s1.dept="BRCC"
s2.name="Kumar"
s2.no=331460
s2.dept="BRCC"
print("The object of S1 before are : ",s1.__dict__)
print("The object of S2 before are : ",s1.__dict__)
print(s1.course)
print(s2.course)
print(student.course)

