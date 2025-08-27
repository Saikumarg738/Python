def sample(val):
    i=1
    while(i<val):
        yield i
        i=i+1

res=sample(7)
print(next(res))
print(next(res))