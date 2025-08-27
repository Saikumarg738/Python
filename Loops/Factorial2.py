n=int(input("Enter How Many Natual Nums Sum u Want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    s,ss,cs=0,0,0 # Additive Identity
    print("-"*60)
    print("\tNat Nums\tSquares\t\t\tCubes")
    print("-" * 60)
    for i in range(1,n+1):
        print("\t{}\t\t\t\t{}\t\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("-" * 60)
        print("\t{}\t\t\t\t{}\t\t\t{}".format(s, ss, cs))
        print("-" * 60)