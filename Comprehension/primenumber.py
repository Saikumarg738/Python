
def prime(a):
    res = True
    a=int(a)
    for i in range(2,a):
        if(a%i==0):
            res=False
            break
    return res

ls=[i for i in input().split() if(prime(i))]

print(ls)