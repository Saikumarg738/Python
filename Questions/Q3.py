#Write a Python program to get the largest number from a list

ls=[36,24,85,34,23,68,7]

largest=0

for num in ls:
    if(num>largest):
        largest=num

print(largest)

# We can also use max


