# Add digits

def digitssum(n):
    if n == 0:
        return n
    else:
        r = n % 10
        return (r + digitssum(n // 10))


# Main Program
res = digitssum(int(input("Enter Numerical Integer Value:")))
print("Digits=", res)