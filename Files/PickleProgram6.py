import pickle

try:
    with open("PP5","rb") as fp:
        data=pickle.load(fp)
        print(data)
except FileNotFoundError:
    print("File not found")
else:
    for i,j in data.items():
        print(f"{i}  :  {j}")
finally:
    print("Thank you")