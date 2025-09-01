import oracledb as orc

try:
    conobj=orc.connect(
        user="admin",
        password="root1234",
        dsn="database-1.cm3s0iaq2072.us-east-1.rds.amazonaws.com/orcl")
    curobj=conobj.cursor()
    sql = """alter table employee
             drop primary key"""
    sql1 ="""alter table employee
           add CONSTRAINT new_pk_name PRIMARY KEY (EID)"""
    try:
        curobj.execute(sql)
    except orc.DatabaseError as er:
        print("Error running query")
        print(er)
    else:
        print("Query executed")
except orc.DatabaseError as err:
    print(err)


