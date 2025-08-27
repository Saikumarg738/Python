#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

n=int(input("Enter number: "))
sign= -1 if n<0 else 1
n=abs(n) # Absolute Value, this convertes negative intergers to positive
n=str(n)
r=n[::-1]
r=int(r)
r=r*sign
print(r)