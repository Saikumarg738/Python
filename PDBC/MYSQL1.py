import mysql.connector as ms

try:
    conobj=ms.connect(
        host='database-1.c41yg8s8qevt.us-east-1.rds.amazonaws.com',
        user='admin',
        passwd='root1234'
    )
    if conobj.is_connected():
        print("Connection established")
    curobj=conobj.cursor()
    query="create DATABASE testdb"
    try:
        curobj.execute(query)
    except ms.DatabaseError as rd:
        print("Error creating the query",rd)
    else:
        print("Query ran succesfully")
except ms.Error as er:
    print("Error connecting",er)