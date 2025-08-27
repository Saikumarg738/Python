def create(a,b,c,cnt="India",**gar):
    print(a)
    print(b)
    print(c)
    for i, j in gar.items():
        print("Key is {}  and value is {}".format(i, j))


create(1,2,3,name="Sai",age="27",job="SE",cnt="USA")