n=int(input("Enter number : "))
v=0
for i in range(2,n):
    if(n%i==0):
        print("{} is not a prime number".format(n))
        break
else:
    print("{} is prime number".format(n))