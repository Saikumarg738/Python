#Print PTON
s="PYTHON"
i=0
while(i<len(s)):
    if(s[i]=="Y" or s[i]=="H"):
        i+=1
        continue
    print(s[i],end="")
    i=i+1