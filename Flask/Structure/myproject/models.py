from myproject import db

class Student(db.Model):

    Name=db.Column(db.String(30),primary_key=True)

    College=db.relationship('College',uselist=False)

    def __init__(self,name):
        self.Name=name

    def __repr__(self):
        if self.College:
            return f"The Student name is {self.Name} and college name is {self.College.Cname}"
        else:
            return f"The Student name is {self.Name} and does not have college"

class College(db.Model):

    Cname=db.Column(db.String(30),primary_key=True)
    Sname=db.Column(db.String(30),db.ForeignKey('student.Name'))

    def __init__(self,Cname,Sname):
        self.Cname=Cname
        self.Sname=Sname