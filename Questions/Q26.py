# Write a python program to check whether two lists are circularly identical.

ls1=[10,20,30,40]
ls2=[40,30,20,10]

print("".join(map(str,ls1)))
print("".join(map(str,ls2)))

if(len(ls1)==len(ls2) and "".join(map(str,ls2)) in "".join(map(str,ls1 * 2))):
    print("They are indentical")
else:
    print("Not")