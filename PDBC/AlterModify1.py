import oracledb as orc

try:
    conobj=orc.connect(
        user="admin",
        password="root1234",
        dsn="database-1.cm3s0iaq2072.us-east-1.rds.amazonaws.com/orcl")
    curobj=conobj.cursor()
    sql="""alter table employee
           modify(EID number(6,2))"""
    sql2="""alter table employee
           modify(Name varchar(30))"""
    try:
        curobj.execute(sql)
        curobj.execute(sql2)
    except orc.DatabaseError as er:
        print("Error running query")
        print(er)
    else:
        print("Query executed")
except orc.DatabaseError as err:
    print(err)


