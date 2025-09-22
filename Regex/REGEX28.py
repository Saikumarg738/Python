import re

mob=input("Enter mobile number")

num=re.search(r"\d{10}",mob)

if(num!=None):
    print(f"{num.group()} is valid number")
else:
    print(f"The number you have entered is invalid")