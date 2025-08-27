
ls1=[ int(a) for a in input("ENter first list : ").split(",")]

ls2=[ int(a) for a in input("ENter first list : ").split(",")]

final=list(map(lambda a,b: a+b, ls1,ls2))

print(final)