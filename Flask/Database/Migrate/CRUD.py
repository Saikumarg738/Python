from BaseModel import myform,db,web

with web.app_context():

    data=myform.query.all()
    for entry in data:
        print(f"{entry.ID} {entry.Name} {entry.Company} {entry.Loc}")