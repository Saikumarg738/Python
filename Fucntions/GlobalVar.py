import pprint

a=10
b=20
c=30

def op():
    a=1
    b=2
    c=3
    print("Printing local")
    print(a)
    print(b)
    print(c)
    obj=globals()
    print("Printing global")
    print(obj['a'])
    print(obj['b'])
    print(obj['c'])
    pprint.pprint(obj)

op()
