# SUm of digits
fin=0
def sum(n,fin=0):
    if(n==0):
        print("The sum is",fin)
    else:
        val=n%10
        fin=fin+val
        n=n//10
        sum(n,fin)

sum(123)

