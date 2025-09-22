import re

data="Hello Sai, Good morning"
si="Sai"

mat=re.search(si,data)

print(mat)
if(mat!=None):
    print(f"Start index is {mat.start()}")
    print(f"End index is {mat.end()}")
    print(f"Match word is {mat.group()}")