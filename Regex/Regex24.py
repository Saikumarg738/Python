import re

data="saishssajaksss"

var=re.finditer("s+",data)

for i in var:
    print(i.group())