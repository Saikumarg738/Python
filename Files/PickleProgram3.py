import pickle
def saverecord():
    with open("emp.pick","ab") as fp:
        while(True):
            print("-"*50)
            empno=int(input("Enter Employee Number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            print("-" * 50)
            #Place the employee values in iterable Object
            lst=list() # create an empty list
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            #Save the Iterable Object data into the file
            pickle.dump(lst,fp)
            print("Employee Record Saved in File Sucessfully")
            print("-" * 50)
            ch=input("Do u want to Insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this program")
                break

#Main Program
saverecord() # Function call