#Sort a list of dictionaries by a key using lambda.

students = [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 91}]

student=sorted(students, key=lambda i: i["score"])

print(student)