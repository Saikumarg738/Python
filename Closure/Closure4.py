
def counter():
    a=0
    def increment():
        nonlocal a
        a=a+1
        return a
    return increment

c=counter()
print(c())
print(c())
print(c())
print(c())
print(c())
print(c())