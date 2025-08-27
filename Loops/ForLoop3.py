#Program for generating all Even Numbers with for loop  where N is +VE

n=int(input("Enter the number: "))
for i in range(1,n):
    if(i%2==0):
        print("The value is {}".format(i))
