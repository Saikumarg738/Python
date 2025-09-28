from functools import reduce

words = ['Hello', 'World', 'from', 'reduce']

concatstr=reduce(lambda x,y: x+y,words)

print(concatstr)