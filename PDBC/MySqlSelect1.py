import mysql.connector as ms

try:
    conobj=ms.connect(
        host="database-1.c41yg8s8qevt.us-east-1.rds.amazonaws.com",
        user="admin",
        passwd="root1234",
        database="testdb"
    )
    curobj=conobj.cursor()
    query="select * from Employee"
    try:
        curobj.execute(query)
        data=curobj.fetchall()
    except ms.DatabaseError as mk:
        print("Error running the query",mk)
    else:
        print("Query Executed")
        for i in data:
            print(f"ID : {i[0]} | Name : {i[1]} | Team : {i[2]} | BU : {i[3]} | TechStack : {i[4]}")
except ms.Error as mk:
    print("Connection not established",mk)
