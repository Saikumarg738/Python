ls=[1,2,3,4,5,6,7,8,9]

def avg(ls):
    a=sum(ls)/len(ls)
    return a

a=list(filter(lambda i: i>avg(ls),ls))

print(a)
