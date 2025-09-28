from fileinput import close

try:
    op=open("Data1","r")
    fs=op.read()
    close()
    with open("Data2","w") as lm:
        lm.write(fs)
except FileExistsError:
    print("File already exists")