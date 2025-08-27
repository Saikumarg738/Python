
def square(take):
    def calculate():
        a=take()
        b=a*2
        c=a**2
        return a,b,c
    return calculate

def takein():
    return int(input("Enter a number : "))

calc=square(takein)

a,b,c=calc()

print("The value of a is {}\nThe value of b is {}\nThe value of c is {}\n".format(a,b,c))