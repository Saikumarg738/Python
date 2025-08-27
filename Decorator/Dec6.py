#Write a decorator that prints "Function is being called" before and after a function is executed.

def deco(samb):
    def wrap():
        print("Function being called")
        samb()
        print("Fucntion being called")
    return wrap

def sama():
    a=10
    b=20
    c=a+b
    print("The total is {}".format(c))

amp=deco(sama)

amp()