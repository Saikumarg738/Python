n=int(input("Enter number : "))
a=0
while(n>0):
    r=n%10
    a=a+r
    n=n//10
print(a)