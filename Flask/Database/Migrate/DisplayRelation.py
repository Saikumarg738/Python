import debugpy.adapter.sessions

from RelationBase import db,Puppy,Toy,Owner,web

with web.app_context():
    # db.create_all()
    # Lab=Puppy("Lab")
    # DM=Puppy("DolMachine")
    # PO=Puppy("Pomerian")
    #
    # db.session.add_all([Lab,DM,PO])
    # db.session.commit()

    puppy=Puppy.query.all()
    for each in puppy:
        print(each)

    # puppydel=Puppy.query.filter(Puppy.id.in_([4,5,6])).all()
    #
    # for pup in puppydel:
    #     db.session.delete(pup)
    #
    # db.session.commit()

    puplab=Puppy.query.filter_by(Name="Lab").first()
    print(puplab)
    # ball=Toy("Ball",puplab.id)
    # bis=Toy("Biscuit",puplab.id
    #
    # db.session.add_all([ball,bis])
    # db.session.commit()

    # Creating owner

    # pupown=Owner("Sai",puplab.id)
    #
    # db.session.add(pupown)
    # db.session.commit()
    # print(puplab)

