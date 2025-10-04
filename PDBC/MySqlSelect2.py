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
            print(f"ID : {i[0]:<8} | Name : {i[1]:<15} | Team : {i[2]:<18} | BU : {i[3]:<6} | TechStack : {i[4]:<15}")
except ms.Error as mk:
    print("Connection not established",mk)
