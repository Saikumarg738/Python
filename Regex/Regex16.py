import re

data="hdjdS@KDEU7483j$sk7HDKJj!dkajd"

si="[^A-Za-z0-9]"

var=re.findall(si,data)

for i in var:
    print(i)