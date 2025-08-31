import oracledb as orc

print(orc.__version__)
try:
    conobj2=orc.connect(
        user="admin",
        password="root1234",
        dsn="database-1.cm3s0iaq2072.us-east-1.rds.amazonaws.com/orcl")
    print("Connection established")
    print(conobj2,type(conobj2))
    curobj=conobj2.cursor()
    print(curobj,type(curobj))
except orc.DatabaseError as dbc:
    print("Connection error : {}".format(dbc))



