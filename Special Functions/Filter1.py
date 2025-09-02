#program for accepting List of Values and Get +Ve Values by using filter()

ls=[int(a) for a in input("Enter list").split()]

pls=list(filter(lambda a: a>0,ls))

print(type(pls))
print(pls)