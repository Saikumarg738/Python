# Checking if a work is vowel or not
word=input("Enter the word : ")
for letter in word:
    if letter.lower() in ["a","e","i","o","u"]:
        print("{} is not a complete consonant".format(word))
        break
else:
    print("{} is complete CONSONANT".format(word))