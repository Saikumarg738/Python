#Accept text of line and exclude vowels and spaces

line=input("Enter the line : ")
for let in line:
    if( let.lower() in ["a","e","i","o","u"," "]):
        continue
    print(let,end="")