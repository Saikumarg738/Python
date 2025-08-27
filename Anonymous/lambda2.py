# Find max number

findmax=lambda a,b: a if a>b else b if b>a else "Both are equal"

print("The bigger number is {}".format(findmax(13,19)))