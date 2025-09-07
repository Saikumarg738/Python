class student:
    @classmethod
    def getcrs(cls):
        cls.course="Python"
        cls.getloc()
    @classmethod
    def getloc(cls):
        student.loc="Hyd"

student.getcrs()
print(student.course)
print(student.loc)
