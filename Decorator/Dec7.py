#Create a decorator that uppercases the output of any function that returns a string.

def deco(samb):
    def wrap():
        print("Function being called")
        c=samb()
        b=c.upper()
        print(b)
    return wrap

def sama():
    c="Hello Sai Gangupamu"
    return c

amp=deco(sama)

amp()