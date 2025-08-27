import pickle

def empadd():
    try:
        name=input("Enter employee name : ")
        id=int(input("Enter employee id : "))
        role=input("Enter Role : ")
    except ValueError:
        print("ID should be numerical")
    else:
        try:
            with open("EmployeeData","ab+") as fl:
                ls=list()
                ls.append(name)
                ls.append(id)
                ls.append(role)
                pickle.dump(ls,fl)
        except FileNotFoundError:
            print("File not found")
        else:
            print("File enter added, details below")
            print(ls)


