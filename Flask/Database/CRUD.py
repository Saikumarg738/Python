from BaseModel import db,mydb,web

with web.app_context():

    dblist=mydb.query.all()
    print(dblist)

    #dblist1=mydb.query.get(3314)

    #dblist1.Name="Sai"

    #db.session.add(dblist1)
    #db.session.commit()

