from BaseEMP1 import Employee,db,app
from Python.Flask.Database.BaseModel1 import Department

with app.app_context():

    emp2=Employee(EMPNAME="Teja",EMPEMAIL="saikumarg7381@gmail.com",EMPSAL="1260000",EMPROLE="Developer")
    db.session.add(emp2)
    db.session.commit()