from BaseModel1 import Department,db,app

with app.app_context():
    deptdata=Department.query.all()

    for i in deptdata:
        print(f"The Department id is {i.Dept_id} and department name is {i.Dept_name}")