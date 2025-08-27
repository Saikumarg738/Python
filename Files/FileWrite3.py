x={"Fname":"Sai","Sname":"Kumar"}
with open("itrobj.data","w+") as fp:
    fp.writelines(x)
    print("Data Written to the File")
    fp.seek(0)
    dt=fp.read()
    print(dt,type(dt))
#    for i in dt:
#        print(i)  # Here list is actually a str so that why ouput is not just values but also [, and ]