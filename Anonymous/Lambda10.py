#Sort a list of tuples by the second element using a lambda.

s=[(2,3),(91,4),(60,23),(34,16),(82,11)]

st=sorted(s, key=lambda i: i[1])

print(st)