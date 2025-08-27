#Write a Python program to find the list of words that are longer than n from a given list of words.

n=int(input("Enter number : "))

ls=["Sai","Kumar","Meghana","Kumari","Gangupamu","Gowda","Malayalam"]
newls=[]
for word in ls:
    if(len(word)>n):
        newls.append(word)
print(" The list is \n {}".format(newls))
