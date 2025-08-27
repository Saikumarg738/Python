ls=["sai","meghna","gangupamu","gowda"]

a=sorted(list(map(lambda i: i.upper(), ls)),key=lambda i:len(i))

print(a)