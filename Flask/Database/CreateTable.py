from BaseModel import db,mydb,web

# Create table

with web.app_context():
    db.create_all()

    sai=mydb(3314,"Sai","BRCC")
    kumar=mydb(3350,"Kumar","MFRS")

    db.session.add(sai)
    db.session.add(kumar)

    db.session.commit()

    print(sai.EID)
