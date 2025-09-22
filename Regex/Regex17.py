import re

data="hdjdS@KDEU7483j$sk7HDKJj!dkajd"

si="\\d"

var=re.findall(si,data)

for i in var:
    print(i)