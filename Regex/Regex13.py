import re

data="hdjdSKDEU7483jsk7HDKJjdkajd"

si="[A-Za-z]"

var=re.findall(si,data)

for i in var:
    print(i)