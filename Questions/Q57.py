#Write a Python program to check if all items of a given list of strings is equal to a given string.

def checkstring(ls,vale):
    #newls=[x for x in ls if x==vale]
    #return newls==ls
    return all(x==vale for x in ls)

print(checkstring(["Sai","Sai","Sai"],"Sai"))