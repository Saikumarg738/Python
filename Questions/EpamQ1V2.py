input=[["dim"],["ate"],["tea"],["eat"],["bat"],["tab"]]

anagram={}

for i in input:
    word = i[0]
    key="".join(sorted(word))
    if(key in anagram):
        anagram[key].append(word)
    else:
        anagram[key]=[word]

print(anagram)

res=[[w for w in group] for group in anagram.values()]
print(res)
