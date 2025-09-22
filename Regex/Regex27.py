import re

text="Rossum is the author of python and whose marks 78, Travis is the author of numpy  and whose marks 68 , Kinney is the author pandas and whose marks 44 and Hunter is the author of matplot lib and whose marks 55 and Gosling the author of java and whose marks 57 and Sai is the student of python and whose marks 62"

lis=re.findall(r"\d{2}",text)

for i in lis:
    print(i)