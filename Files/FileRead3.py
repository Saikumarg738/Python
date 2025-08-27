try:
    name=input("Enter filename : ")
    with open(name,"r") as a:
        data=a.read()
        print(data,end="")
except FileNotFoundError:
    print("File not found")