import re

data="hdjdS@KDEU7483j$sk7HDKJj!dkajd"

si=r"\W"

var=re.findall(si,data)

for i in var:
    print(i)