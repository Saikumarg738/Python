
input=["dim","ate","tea","eat","bat","tab"]

anagram={}
for i in input:
    key="".join(sorted(i))
    if key in anagram:
        anagram[key].append(i)
    else:
        anagram[key]=[i]

print(list(anagram.values()))