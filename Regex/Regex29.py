#Extracting names
import re

data="Rossum is the author of python, Travis is the author of numpy , Kinney is the author pandas and Hunter is the author of matplot lib and Gosling the author of java and Sai is the student of python"

name="[A-Z][a-z]+"

names=re.findall(name,data)

for i in names:
    print(i)