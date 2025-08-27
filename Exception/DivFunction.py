from DivException import MyDivException

def div(a,b):
    if(b==0):
        raise MyDivException
    c=a/b
    return c