try:
    a=open("Sai.py","r")
except FileNotFoundError:
    print("File does not exists")
else:
    print("Something")
finally:
    try:
        fp.close()
    except NameError:
        print("FIle is not opened so no need to close")