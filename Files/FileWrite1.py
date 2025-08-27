try:
    a=open("Data1","w")
    name="Sai"
    Age=27
    Job="SE"
    a.write(name+"\n")
    a.write(str(Age)+"\n")
    a.write(Job+"\n")
except FileNotFoundError:
    print("No file")