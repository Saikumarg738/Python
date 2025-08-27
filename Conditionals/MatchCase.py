print("Enter 1 for addition")
print("Enter 2 for substraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")

val=int(input("Enter value : "))

match(val):
    case 1:
        a=int(input("Enter first value : "))
        b=int(input("Enter second value : "))
        print("The addition is {}".format(a+b))
    case 2:
        a = int(input("Enter first value : "))
        b = int(input("Enter second value : "))
        print("The sub is {}".format(a-b))
    case 3:
        a = int(input("Enter first value : "))
        b = int(input("Enter second value : "))
        print("The mul is {}".format(a * b))
    case 4:
        a = int(input("Enter first value : "))
        b = int(input("Enter second value : "))
        print("The div is {}".format(a/b))
    case _:
        print("Correct value enter cheyi ra pulka")

