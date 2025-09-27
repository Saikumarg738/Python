# Armstrong number

num=input("Enter number")

ls=[int(i) for i in num]

newls=map(lambda i:i**3,ls)

print("Armstrong" if int(num)==sum(newls) else "It is not armstrong")