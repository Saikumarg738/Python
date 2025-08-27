# Generate all odd number in reverse regarless of what value we give
n=int(input("Enter number: "))
if(n%2==0):
    n-=1
for i in range(n,0,-2):
    print("Odd number is : {}".format(i))