from BaseModel1 import db,app,Department

with app.app_context():

    # db.create_all()
    #
    # o1=Department("Dev")
    #
    # db.session.add(o1)
    #
    # db.session.commit()
    #Users=Department.query.filter_by(Dept_name="Devops").all()
    #for i in Users:
    #    print(i.Dept_id,i.Dept_name)

    c=Department.query.count()
    print(c)