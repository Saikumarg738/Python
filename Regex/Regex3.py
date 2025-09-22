import re

data="Hello sai kumar gangupamu, How are you, How is life, how is everything"

si="How"

var=re.finditer(si,data)

for i in var:
    print(i)