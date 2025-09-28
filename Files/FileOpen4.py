try:
    with open("Sample.txt","a+") as fa:
        print("Is file open? : ",fa.closed)
        print("File mode : ",fa.mode)
        print("Is file readable? : ",fa.readable())
        print("Is file writable? : ",fa.writable())
        print("Name of the file : ",fa.name)
except FileNotFoundError:
    print("No file")
except FileExistsError:
    print("File already exists")