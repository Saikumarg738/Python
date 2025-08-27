
def disp(a,b,c,*d,city="Hyd"):
    print(a)
    print(b)
    print(c)
    s=0
    for i in d:
        s=s+i
    print("Sum is "+ str(s))
    print(city)

disp("SAi","Kumar","Gan",3,4,5,6,7,1,city="VZG")