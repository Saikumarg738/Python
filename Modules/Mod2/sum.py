from functools import reduce
def calsum(*a):
    res=reduce(lambda a,b:a+b,a)
    return res
