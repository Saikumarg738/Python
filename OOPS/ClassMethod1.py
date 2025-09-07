class student:
    @classmethod
    def getdetail(cls):
        cls.course="PYTHON"
        student.dur=6

student.getdetail()
print("The course name is {}".format(student.course))