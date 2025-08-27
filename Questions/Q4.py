#Write a Python program to get the smallest number from a list.
ls=[36,24,85,34,23,68,7]

smallest=ls[0]

for num in ls:
    if(num<smallest):
        smallest=num
print(smallest)

# We can also use min