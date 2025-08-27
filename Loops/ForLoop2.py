n=int(input("The the number: "))
if ( n>=0):
    print("Number is positive so proceed with execution")
    for i in range(n,0,-1):
        print("The value is {}".format(i))
else:
    print("Number is negative so not executing")