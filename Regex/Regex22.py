import re

data="hdjdS@KD EU7483j $sk7HDKJj!d kajd"

si=r"\S"

var=re.findall(si,data)

for i in var:
    print(i)