import pickle
def readrecords():
    try:
        print("-"*50)
        with open("emp.pick","rb") as fp:
            record=pickle.load(fp)
            print(record)
    except FileNotFoundError:
        print("File Does not Exist")

#Main Program
readrecords()