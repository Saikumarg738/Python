# Take 2 lists and add number

ls1=[int(i) for i in input("Enter the list with .").split(".")]

ls2=[int(i) for i in input("Enter the list with .").split(".")]

sumls=list(map(lambda a,b: a+b, ls1, ls2))

print(sumls)