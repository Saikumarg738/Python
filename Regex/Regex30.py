import re

with open("C:\\Python text files\\Python1.txt","r") as fp:
    filedata=fp.read()
    names=re.findall(r"[A-Z][a-z]+",filedata)
    emails=re.findall(r"\S+@\S+",filedata)
    for i in names:
        print(f"The name is {i}")
    for i in emails:
        print(f"The email is {i}")
