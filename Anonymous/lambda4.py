

def prime(n):
    ans=True
    n=int(n)
    for i in range(2,n):
        if(n%i==0):
            ans=False
            break
    if(ans==True):
        return "Prime"
    else:
        return "False"

findprime=lambda a:prime(a)

ls=[i for i in input("Find prime numbers : ").split() if(findprime(i)=="Prime")]

print("List of prime numbers are {}".format(ls))