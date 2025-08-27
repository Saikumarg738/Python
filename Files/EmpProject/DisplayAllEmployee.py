import pickle

def displayall():
    with open("EmployeeData","rb") as fl:
        while(True):
            try:
                record=pickle.load(fl)
                print(record)
            except EOFError:
                break

displayall()

