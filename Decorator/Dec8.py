#Create a decorator that uppercases the output of any function that returns a string.

def deco2(wrap):
    def wrap2(*nam):
        print("Lower case")
        b=wrap(*nam)
        print("Upper case is {}".format(b))
        d=b.lower()
        print("Lower case is {}".format(d))
    return wrap2

def deco(samb):
    def wrap(name):
        print("Function being called")
        c=samb(name)
        b=c.upper()
        return b
    return wrap

@deco2
@deco
def sama(name):
    c="Hello"+name
    return c

sama("Sai kumar gangupamu")