words = ["apple", "banana", "kiwi"]

words=sorted(words, key=lambda i: len(i))

# key will tell python how to sort the given iterable object
print(words)