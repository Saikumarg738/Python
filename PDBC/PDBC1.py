import mysql.connector

print(mysql.connector.__file__)
print(mysql.connector.__version__)
try:
    conobj=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="root1234"
    )
    curobj=conobj.cursor()
    print("Connection object is of {}".format(type(conobj)))
    print("Cursr object is of {}".format(type(curobj)))
    curobj.close()
    conobj.close()
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))


