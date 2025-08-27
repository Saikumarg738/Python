import pickle

def save():
    with open("PickleData1","ab") as pk:
        try:
            name=input("Enter name : ")
            age=int(input("Enter age : "))
            sal=int(input("ENter salary : "))
        except ValueError:
            print("Please enter only digits")
        else:
            ls=list()
            ls.append(name)
            ls.append(age)
            ls.append(sal)
            pickle.dump(ls,pk)

save()
