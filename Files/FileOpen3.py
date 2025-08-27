try:
    with open("Sample.data","r") as fp:
        print("Inside file")
        print("Is file closed?",fp.closed)
    print("I am outside of open")
    print("Is file closed?",fp.closed)
except FileNotFoundError:
    print("File could not be found")