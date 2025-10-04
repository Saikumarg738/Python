import mysql.connector as ms

try:
    conobj=ms.connect(
        host="database-1.c41yg8s8qevt.us-east-1.rds.amazonaws.com",
        user="admin",
        passwd="root1234",
        database="testdb"
    )
    curobj=conobj.cursor()
    query="""Insert into Employee (ID,Name,Team,BU,TechStack)
             values (331460,'Gangupamu','Output Services','BRCC','Jenkins and CICD'),
             (331461,'Teja','Output Services','BRCC','Docker and Kubernetes')"""
    try:
        curobj.execute(query)
        conobj.commit()
    except ms.DatabaseError as mk:
        print("Error running the query",mk)
    else:
        print("Query Executed")
except ms.Error as mk:
    print("Connection not established",mk)
