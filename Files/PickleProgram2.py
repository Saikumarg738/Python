import pickle

try:
    with open("PickleData1","rb") as op:
        record=pickle.load(op)
        print(record)
        for i in record:
            print(i,end="\t")
except FileNotFoundError:
    print("File not found")