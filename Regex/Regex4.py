import re

data="Hello Kumar, how are you, good to see you Kumar"

newdata=re.sub("Kumar","Sai",data)

print(data)
print(newdata)