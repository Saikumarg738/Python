from fileinput import close

try:
    op=open("Data1","r")
    fs=op.read()
    close()
    with open("Data2","w") as lm:
        lm.writelines(fs)
except FileExistsError:
    print("File already exists")