# Skip H
s="PYTHON"
i=0
while(i<len(s)):
    if(s[i]=="H"):
        i += 1
        continue
    print(s[i],end="")
    i += 1