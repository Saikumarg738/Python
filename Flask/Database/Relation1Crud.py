from Relation1base import app,db,Department,Employee

with app.app_context():

    e1=Employee.query.all()
    for i in e1:
        print(i.id,i.name,i.department_id)