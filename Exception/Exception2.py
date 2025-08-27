try:
    a=int(input("Enter value : "))
    b=int(input("Enter second value : "))
    c=a/b
    s="SAIGAN"
    s[10]
except ZeroDivisionError:
    print("DOn't enter den as 0")
except ValueError:
    print("Enter num")
except IndexError:
    print("Indez not availa")