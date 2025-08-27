#List prime number within given range

rangeval=int(input("Enter Range in which u want primes:"))
if(rangeval<=1):
    print("\t{} is Invalid Input".format(rangeval))
else:
    print("-"*50)
    print("List of Primes within {}".format(rangeval))
    print("-" * 50)
    for num in range(2,rangeval+1):#outer loop--supply the number
        result=True
        for i in range(2,num):
            if(num%i==0):
                result=False
                break
        if(result):
            print("\t\t{}".format(num))
    print("-" * 50)
