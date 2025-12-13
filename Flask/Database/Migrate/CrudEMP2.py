from BaseEMP2 import Employee,db,app
from Python.Flask.Database.BaseModel1 import Department

with app.app_context():

    #db.create_all()

    #emp2=Employee(EMPNAME="Teja",EMPEMAIL="saikumarg7381@gmail.com",EMPSAL="1260000")
    #db.session.add(emp2)
    #db.session.commit()

    #empdata=Employee.query.all()
    #print(empdata)

    #emp3=Employee(EMPNAME="Sai",EMPEMAIL="saikumarg738@gmail.com",EMPSAL="1290000",EMPROLE="Dev")
    #db.session.add(emp3)
    #db.session.commit()

    users=Employee.query.all()
    for i in users:
        print(i)


