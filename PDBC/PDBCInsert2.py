import oracledb as orc

try:
    conobj=orc.connect(
        user="admin",
        password="root1234",
        dsn="database-1.cm3s0iaq2072.us-east-1.rds.amazonaws.com/orcl")
    curobj=conobj.cursor()
    #sql="""insert into employee (Name,Dept,Role,Exp,EID)
    #      values('Meghna Kumari','BRCC','SMT',5.8,331460)"""
    sql="""insert into employee (Name,Dept,Role,Exp,EID)
           values('Ram charan','TFI','Global Star',9,331461)"""
    try:
        curobj.execute(sql)
        conobj.commit()
    except orc.DatabaseError as er:
        print("Error running query")
        print(er)
    else:
        print("Query executed")
except orc.DatabaseError as err:
    print(err)


