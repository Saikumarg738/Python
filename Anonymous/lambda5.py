word=input("Enter the word : ")

val=lambda wd:"".join(sorted(wd,reverse=True))

order=val(word)

print("The sorted order of word is {}".format(order))