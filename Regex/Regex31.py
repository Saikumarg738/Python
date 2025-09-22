#Extracting names and marks
import re

data="Rossum is the author of python and whose marks 78, Travis is the author of numpy  and whose marks 68 , Kinney is the author pandas and whose marks 44 and Hunter is the author of matplot lib and whose marks 55 and Gosling the author of java and whose marks 57 and Sai is the student of python and whose marks 62"

names=re.findall(r"[A-Z][a-z]+",data)
marks=re.findall(r"\d{2}",data)

for i,j in zip(names,marks):
    print(f"Student {i} has got {j} marks")

