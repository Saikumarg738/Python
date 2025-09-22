import re

data="hdjdSKDEU7483jsk7HDKJjdkajd"

si="[0-9]"

var=re.findall(si,data)

for i in var:
    print(i)