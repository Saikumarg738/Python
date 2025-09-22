import re

data="hdjdSKDEU7483jsk7HDKJjdkajd"

si="[a-z]"

var=re.findall(si,data)

for i in var:
    print(i)