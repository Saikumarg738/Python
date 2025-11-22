#Write a Python program to check whether a list contains a sublist

ls=[1,2,3,4,5,6,7,8,9]

sub=[3,4,5]
'''val=False
for i in range(len(ls)-len(sub)+1):
    if(ls[i:i+len(sub)]==sub):
        val=True
        break

print(val)'''

val=any(ls[i:i+len(sub)]==sub for i in range(len(ls)-len(sub)+1))
print(val)

