try:
    a=open("C:\\Users\\GangupamuS\\PyCharmMiscProject\\Python\\Files\\Sample.txt","r")
    data=a.readlines()
    print(data)
    for r in data:
        print(r,end="")
except FileNotFoundError:
    print("No file")