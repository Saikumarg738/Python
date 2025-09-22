import re

data="andjtbdjgfkcigu"

si="[^abc]"

var=re.finditer(si,data)

for i in var:
    print(f"Start Index : {i.start()}  End Index : {i.end()}  Matched word : {i.group()}")