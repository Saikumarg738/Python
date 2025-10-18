from BaseModel import myform,db,web


with web.app_context():

    db.create_all()

    sai=myform(1,"Sai","Broadridge","HYD")
    gyani=myform(2,"Gyani","Evernorth","HYD")
    srikar=myform(3,"Srikar","TCS","HYD")
    Sahith=myform(4,"Sahith","Delloite","HYD")

    db.session.add_all([sai,gyani,srikar,Sahith])
    db.session.commit()