#program for accepting List of words and Get Only Panlindrome Words

ls=[a for a in input().split()]

print(ls)

fls=list(filter(lambda a: a[::]==a[::-1],ls))

print(fls)