#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

sqls=[]
for i in range(1,31):
    sqls.append(i**2)
print(sqls)
fls=sqls[0:5]
lls=sqls[len(sqls)-6:len(sqls)]
print(fls)
print(lls)