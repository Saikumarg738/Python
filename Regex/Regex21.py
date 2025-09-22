import re

data="hdjdS @KDEU74 83j$sk7HDK Jj!dkajd"

si=r"\s"

var=re.findall(si,data)

for i in var:
    print(i)