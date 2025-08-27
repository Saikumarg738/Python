import pickle

#def deleteemployee():
#    name = input("Enter Employee name to Delete:")
#    # get all the records from File
#    records = []  # for adding records--outer list
#    with open("EmployeeData", "rb") as fp:
#        while (True):
#            try:
#                record = pickle.load(fp)
#                records.append(record)
#            except EOFError:
#                break
#    found=False
#    for recindex in range(len(records)):
#        if(records[recindex][0]==name):
#            index=recindex
#            found=True
#            break
#    if(found):
#        #delete the record by using pop(index)
#        records.pop(index)
#        print("\tEMPLOYEE RECORD DELETED")
#        #After Removing the Records, Save the Remaining in file by replacing the existing Records
#        with open("EmployeeData","wb") as fp:
#            for record in records:
#                  pickle.dump(record,fp)
#    else:
#        print("\tEMPLOYEE RECORD DOES NOT EXIT")
#
#deleteemployee()

def empdel():
    name=input("Enter employee name : ")
    records=[]
    try:
        with open("EmployeeData", "rb") as fl:
            while(True):
                try:
                    record=pickle.load(fl)
                    records.append(record)
                except EOFError:
                    break
    except FileNotFoundError:
        print("FIle not found")
    else:
        for val in records:
            if(val[0]==name):
                records.remove(val)
                break
        else:
            print("Employee not found")
        with open("EmployeeData","wb") as fl:
            for a in records:
                pickle.dump(a,fl)




