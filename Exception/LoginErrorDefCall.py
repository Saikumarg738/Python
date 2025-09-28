from LoginErrorDef import *

try:
    username=input("Enter your username : ")
    password=input("Enter your password : ")
    checkcred(username,password)
except InvalidLoginException:
    print("Incorrect credentials")
else:
    print("Login succesfull")
finally:
    print("Thank You for visiting")