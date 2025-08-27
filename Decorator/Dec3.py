#Using Decorator

def sqrt(salaar):
    def calc():
        a,n=salaar()
        s=a**0.5
        return a,n,s
    return calc

def sq(salaar):
    def calc():
        a=salaar()
        n=a**2
        return a,n
    return calc

@sqrt
@sq
def deva():
    return int(input("Enter number : "))

a,n,s=deva()

print("Square of a is {}".format(n))
print("Square root of a is {}".format(s))

