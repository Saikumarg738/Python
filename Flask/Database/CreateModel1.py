from BaseModel1 import db,app,Department

with app.app_context():

    db.create_all()

    o1=Department("Dev")

    db.session.add(o1)

    db.session.commit()

