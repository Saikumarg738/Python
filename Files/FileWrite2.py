try:
    with open("Data1","a+") as fl:
        name=input("Enter name : ")
        age=input("Enter age : ")
        job=input("Enter job : ")
        fl.write(name+"\n")
        fl.write(age+"\n")
        fl.write(job+"\n")
        fl.seek(0)
        data=fl.read()
        print(data)
except FileNotFoundError:
    print("File not found")