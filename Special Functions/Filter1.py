#program for accepting List of Values and Get +Ve Values by using filter()

ls=[int(a) for a in input().split()]

pls=filter(lambda a: a>0,ls)

pls=list(pls)

print(pls)