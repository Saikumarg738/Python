
glcount=0
def dec(inp):
    def decotared():
        global glcount
        glcount+=1
        fname=inp()
        print((fname,glcount))
    return decotared


def call():
    return call.__name__

decret=dec(call)

decret()
decret()
decret()
decret()
decret()