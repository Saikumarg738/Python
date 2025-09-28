from functools import reduce

a=[5,2,8,9,5,3,7]

b=reduce(lambda g,f: g if g>f else f,a)

print(b)