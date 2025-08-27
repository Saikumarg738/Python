try:
    r=open("C:\\Users\\GangupamuS\\PyCharmMiscProject\\Python\\Files\\Sample.txt","r")
    print("Hello Sai, please find data below")
    data=r.read()
    print(type(data))
    print(data)
except FileNotFoundError:
    print("FIle not opening")