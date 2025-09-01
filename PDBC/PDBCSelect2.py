import oracledb as orc

try:
    conobj=orc.connect(
        user="admin",
        password="root1234",
        dsn="database-1.cm3s0iaq2072.us-east-1.rds.amazonaws.com/orcl")
    curobj=conobj.cursor()
    sql="""Select * from employee"""
    try:
        curobj.execute(sql)
        while(True):
            data=curobj.fetchone()
            if(data!=None):
                for i in data:
                    print(i,end="\t")
                print()
            else:
                break
    except orc.DatabaseError as er:
        print("Error running query")
        print(er)
    else:
        print("Query executed")
except orc.DatabaseError as err:
    print(err)


