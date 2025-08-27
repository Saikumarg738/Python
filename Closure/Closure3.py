a=10
def mainf(x):
    b=15
    def innerf(y):
        global a
        nonlocal b,x
        print("The pre values of A,B,X,Y are {},{},{},{}".format(a, b, x, y))
        a=a+5
        b=b+5
        x=x+5
        y=y+5
        print("The post values of A,B,X,Y are {},{},{},{}".format(a,b,x,y))
    return innerf

cal=mainf(20)

cal(25)
cal(30)
cal(35)