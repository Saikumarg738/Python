while(True):
    try:
        a=int(input("Enter a value : "))
        b=int(input("Enter b value : "))
        res=a/b
    except ZeroDivisionError:
        print("Den should not be zero")
    else:
        print("Result is",res)
        break
    finally:
        print("Program ended")