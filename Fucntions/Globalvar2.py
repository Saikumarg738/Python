a=10
b=20

def op():
    obj=globals()
    print("*****  1  *******")
    print("The value of a : {}\nThe value of b : {}".format(obj['a'],obj['b']))
    print("*****  2  *******")
    print("The value of a : {}\nThe value of b : {}".format(obj.get('a'),obj.get('b')))

op()

